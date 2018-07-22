# coding=utf-8

import datetime
import random
import os
import sys
import json

from battle.battle2.squad import Squad
from battle.battle2.unit import Unit

from battle_calculate import hit, shuffle

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "sg.settings")

application = get_wsgi_application()

from battle.models import Battle, BattleProcess


class BattleField(object):
    def __init__(self, home_squad, away_squad):
        self.home_squad = home_squad
        self.away_squad = away_squad
        self.round = 0
        self.home_units_list = []
        self.away_units_list = []

        self.init_squad()
        self.action_queue = self.make_action_queue()

    def eliminate_unit(self, target):
        """
        消灭unit，去掉action_queue home_units_list away_units_list 中对应的单位
        """
        if target.get_belong() == "home":
            self.home_units_list.remove(target)
        else:
            self.away_units_list.remove(target)
        self.action_queue.remove(target)
        # print len(self.home_units_list),len(self.away_units_list),len(self.action_queue)
        # pass

    def make_action_queue(self):
        all_player = self.home_units_list + self.away_units_list
        return shuffle(all_player)

    def init_squad(self):
        home_units_list = self.home_squad.get_units()
        for unit in home_units_list:
            count = unit["count"]
            unit_class = unit["Unit"]
            for i in range(1, count + 1):
                belong = "home"
                unit_name = unit_class.__name__ + "_" + str(i)
                self.home_units_list.append(unit_class(unit_name, belong))

        away_units_list = self.away_squad.get_units()
        for unit in away_units_list:
            count = unit["count"]
            unit_class = unit["Unit"]
            for i in range(1, count + 1):
                belong = "away"
                unit_name = unit_class.__name__ + "_" + str(i)
                self.away_units_list.append(unit_class(unit_name, belong))

        # print self.away_units_list[1]

    def chose_target(self, unit):
        belong = unit.get_belong()
        if belong == "home":
            pool = self.away_units_list
        else:
            pool = self.home_units_list
        return random.choice(pool)

    def get_attack_result(self, unit, target):
        acc = unit.get_attack_accuracy()
        h = hit(acc)
        return h

    def unit_move_end(self, unit, target, move, result):
        if move == "attack":
            if result:
                self.eliminate_unit(target)

    def check_battle_finish(self):
        if len(self.away_units_list) == 0 or len(self.home_units_list) == 0:
            return True

        return False

    def battle_result(self):
        """
        战斗结果
        """
        total_round = self.round
        if len(self.away_units_list) == 0:
            winer = "home"
        elif len(self.home_units_list) == 0:
            winer = "away"
        else:
            raise Exception("battle_result")

        # 整理剩下单位
        home_remaind = []
        home_dict, away_dict = {}, {}
        for i in self.home_units_list:
            unit_class = i.__class__
            if unit_class in home_dict.keys():
                home_dict[unit_class] += 1
            else:
                home_dict[unit_class] = 1
        # print home_dict

        for i in self.away_units_list:
            unit_class = i.__class__
            if unit_class in away_dict.keys():
                away_dict[unit_class] += 1
            else:
                away_dict[unit_class] = 1
        # print away_dict

        home_casualties, away_casualties = {}, {}
        for i in self.home_squad.units:
            unit_class, count = i["Unit"], i["count"]
            remain = home_dict.get(unit_class, 0)
            lost_count = count - remain
            home_casualties[unit_class.__name__] = lost_count
        for i in self.away_squad.units:
            unit_class, count = i["Unit"], i["count"]
            remain = away_dict.get(unit_class, 0)
            lost_count = count - remain
            away_casualties[unit_class.__name__] = lost_count

        result = {"total_round": total_round, "winner": winer, "home_casualties": home_casualties,
                  "away_casualties": away_casualties}
        return result

    def battle_process_log(self, battle_id, round, belong, unit, target, move, result):
        BattleProcess.add_data(battle_id, round, belong, unit, target, move, result)

    def battle_result_log(self, battle_id, battle_result):
        start_date = datetime.date.today()
        home = self.home_squad.squad_name
        away = self.away_squad.squad_name
        winner = battle_result.get("winner")
        home_casualties = json.dumps(battle_result.get("home_casualties"))
        away_casualties = json.dumps(battle_result.get("away_casualties"))
        Battle.add_data(battle_id, start_date, home, away, winner, home_casualties, away_casualties)

    def init_battle_log(self, start_date, home, away):
        return Battle.init(start_date, home, away)

    def start_fight(self):
        battle_id = self.init_battle_log(datetime.date.today(), self.home_squad.squad_name, self.away_squad.squad_name)
        while True:
            if self.check_battle_finish():
                break
            self.round += 1
            print "round: ", self.round, "home units:", len(self.home_units_list), "away units:", len(
                self.away_units_list), datetime.datetime.now()
            for unit in self.action_queue:
                belong = unit.get_belong()
                print belong, unit,
                move = unit.move()
                if move == "attack":
                    print "attacking",
                    target = self.chose_target(unit)
                    print "target:", target.get_belong(), target,
                    hit = self.get_attack_result(unit, target)
                    print "hit:", hit
                    self.unit_move_end(unit, target, move, hit)
                    if hit:
                        result = "hit"
                    else:
                        result = "miss"
                self.battle_process_log(battle_id, self.round, belong, unit, target, move, result)
                if self.check_battle_finish():
                    break

        battle_result = self.battle_result()
        print battle_result
        self.battle_result_log(battle_id, battle_result)


if __name__ == '__main__':
    print "qq"
    home_squad = Squad("home_squad", [{"Unit": Unit, "count": 10}])
    away_squad = Squad("away_squad", [{"Unit": Unit, "count": 10}])
    a = BattleField(home_squad, away_squad)
    a.start_fight()
