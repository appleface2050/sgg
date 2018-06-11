# coding=utf-8

import datetime

from battle_sim.battle_ground import BattleGround

from battle_sim.battle_team import BattleTeam
from battle_sim.soldier import InfantrySoldier

from battle_sim.infantry_outfit import drill_outfit001

if __name__ == '__main__':
    # soldier = InfantrySoldier(drill_outfit001)
    home = BattleTeam([InfantrySoldier(drill_outfit001)])
    away = BattleTeam([InfantrySoldier(drill_outfit001)])
    battle = BattleGround(home, away)
    battle.team_describe()


