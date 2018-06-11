# coding=utf-8
from util.baseclass import Gear


class Cloth(Gear):
    """
    挂载系统
    """
    class Meta:
        abstract = True

    def __init__(self):
        self.name = ""
        self.weight = 0.0
        self.long_gun_slot = 0
        self.short_gun_slot = 0
        self.grenade_slot = 0
        self.long_gun_cartridge_slot = 0
        self.short_gun_cartridge_slot = 0

    def get_long_gun_cartridge_slot(self):
        return self.long_gun_cartridge_slot

    def get_short_gun_cartridge_slot(self):
        return self.short_gun_cartridge_slot


class Mk001(Cloth):
    """
    MK001标准挂载
    """
    def __init__(self):
        self.name = "MK001"
        self.weight = 4.5
        self.long_gun_slot = 1
        self.short_gun_slot = 1
        self.grenade_slot = 6
        self.long_gun_cartridge_slot = 8
        self.short_gun_cartridge_slot = 4

class Mk002(Cloth):
    """
    MK002手枪挂载
    """
    def __init__(self):
        self.name = "MK002"
        self.weight = 4.5
        self.long_gun_slot = 0
        self.short_gun_slot = 1
        self.grenade_slot = 6
        self.long_gun_cartridge_slot = 0
        self.short_gun_cartridge_slot = 12



#############Instance####################
cloth_mk001 = Mk001()
cloth_mk002 = Mk002()

if __name__ == '__main__':
    print cloth_mk002.name