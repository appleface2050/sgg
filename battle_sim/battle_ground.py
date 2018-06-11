# coding=utf-8

import datetime


class BattleGround(object):
    def __init__(self, home, away, home_tactics, away_tactics):
        self.home = home
        self.away = away
        self.home_tactics = ""
        self.away_tactics = ""
        self.round = 0


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

