# coding=utf-8

from battle.battle2.battlefield import BattleField
from battle.battle2.squad import Squad
from battle.battle2.unit import Unit

class BattleSim(object):
    def sim_N_battle(self, N, home_squad, away_squad):
        for i in range(N):
            a = BattleField(home_squad, away_squad)
            a.start_fight()

if __name__ == '__main__':
    home_squad = Squad("home_squad", [{"Unit": Unit, "count": 10}])
    away_squad = Squad("away_squad", [{"Unit": Unit, "count": 10}])
    a = BattleSim()
    a.sim_N_battle(99, home_squad, away_squad)