# coding=utf-8


from battle.battle2.unit import Unit

class Squad(object):
    """
    阵容
    """
    def __init__(self, squad_name, units):
        self.squad_name = squad_name
        self.units = units   #[{"Unit": Unit ,"count": 0}]

    def get_units(self):
        return self.units








