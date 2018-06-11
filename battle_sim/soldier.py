# coding=utf-8
from battle_sim.infantry_outfit import drill_outfit001


class InfantrySoldier(object):
    """
    士兵
    """
    def __init__(self):
        self.out_fit = drill_outfit001
        self.weight = self.out_fit.get_weight()

if __name__ == '__main__':
    a = InfantrySoldier()
    print a.weight