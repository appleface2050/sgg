# coding=utf-8

import datetime

class BattleGroundTeamStatus(object):
    """
    战斗时team状态
    """
    def __init__(self):
        pass

class BattleGroundSoldierStatus(object):
    """
    战斗时个体状态
    """
    def __init__(self):
        self.body = "normal"
        self.weapon = "normal"
        self.target = None
        self.distance = None
        self.action = None
        self.blindage = False
        self.passive_status = []

        self.target_by = None
        # self.distance_by = None


class BattleGround(object):
    def __init__(self, home, away, home_tactics, away_tactics):
        self.home = home
        self.away = away
        self.home_tactics = ""
        self.away_tactics = ""
        self.home_team_status = {}
        self.away_team_status = {}
        self.round = 0
        self.action_quene = []

    def update_action_quene(self):
        """
        更新行动顺序
        """

    def team_describe(self):
        print "===team describe==="
        print "!!!Home!!!"
        for i in self.home.soldiers:
            print i
        print "!!!Away!!!"
        for i in self.away.soldiers:
            print i
        print "===end team describe==="

    def start(self):
        print "combat start"


    # def combat(self):

