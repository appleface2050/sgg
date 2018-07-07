# coding=utf-8

import datetime

from battle.battle_.battle_soldier import BattleSoldier
from battle.battle_.squad import Squad
from battle.battle_.weapon_package import WeaponPackageSim001
from util.fun_ import shuffle


class BattleField(object):
    """
    战场
    """

    def __init__(self, home_squad, away_squad):
        self.home_name = home_squad.team_name
        self.away_name = away_squad.team_name

        self.home_players = home_squad.players_list
        self.away_player = away_squad.players_list

        # 距离
        self.distance_set = set([])

        # 行动顺序
        self.action_queue = self.make_action_queue()
        print self.action_queue

        self.round = 0

    def make_action_queue(self):
        all_player = self.home_players + self.away_player
        return shuffle(all_player)

    def begin(self):
        while True:
            self.round += 1
            print "start round: ", self.round, datetime.datetime.now()
            for player in self.action_queue:
                move = player.make_move()
                print move
                action_type = move.get("action_type")
                target = move.get("target")
                weapon = move.get("weapon")

                if action_type == "SEARCHING":
                    pass
                elif action_type == "APPROACHING":
                    pass
                elif action_type == "ATTACKING":
                    pass
                elif action_type == "RETREAT":
                    pass

                player.do_update()
            if self.round >= 10:
                break


if __name__ == '__main__':
    squad_home = Squad("sim_home",
                       [BattleSoldier("home_player1", WeaponPackageSim001()),
                        BattleSoldier("home_player2", WeaponPackageSim001()),
                        BattleSoldier("home_player3", WeaponPackageSim001())
                        ])
    squad_away = Squad("sim_away",
                       [BattleSoldier("away_player1", WeaponPackageSim001()),
                        BattleSoldier("away_player2", WeaponPackageSim001()),
                        BattleSoldier("away_player3", WeaponPackageSim001())
                        ])

    battle_field = BattleField(squad_home, squad_away)
    battle_field.begin()
