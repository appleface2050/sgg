# coding=utf-8
from battle_sim.cloth import cloth_mk002
from battle_sim.firearms import glock17
from util.baseclass import Gear


class InfantryOutfit(Gear):
    """
    步兵装备模板
    """
    class Meta:
        abstract = True

    def __init__(self):
        self.cloth = None
        self.long_gun = None #当前只能装备一个
        self.short_gun = None #当前只能装备一个
        self.grenade = []

        self.check_cloth_slot_correct()

        self.weight = self.cal_weight()
        self.long_gun_bullet_amount = self.cal_gun_bullet_amount(self.long_gun, "long_gun")
        self.short_gun_bullet_amount = self.cal_gun_bullet_amount(self.short_gun, "short_gun")

    def cal_weight(self):
        """
        计算装备重量
        """
        cloth_weight =  self.cloth.get_weight()
        long_gun_weight, short_gun_weight = 0.0 ,0.0
        if self.long_gun:
            long_gun_weight = self.long_gun.get_weight()
        if self.short_gun:
            short_gun_weight = self.short_gun.get_weight()
        return cloth_weight+long_gun_weight+short_gun_weight

    def cal_gun_bullet_amount(self, gun, gun_type):
        cartridge_slot = 0
        if gun_type == "long_gun":
            cartridge_slot = self.cloth.get_long_gun_cartridge_slot()
        elif gun_type == "short_gun":
            cartridge_slot = self.cloth.get_short_gun_cartridge_slot()
        else:
            raise Exception("cal gun bullet amount fail")

        if gun and self.cloth:
            return gun.get_cartridge_capacity() * cartridge_slot
        else:
            return 0


    def check_cloth_slot_correct(self):
        """
        检查装备是否符合cloth
        """
        correct = True
        if self.cloth.grenade_slot < len(self.grenade):
            correct = False
        # if self.cloth.long_gun_slot < len(self.long_gun):
        #     correct = False
        # if self.cloth.short_gun_slot < len(self.short_gun):
        #     correct = False
        if not correct:
            raise Exception("check cloth slot fail")

class DrillInfantryOutfit001(InfantryOutfit):
    """
    演习001装备 手枪装备
    """
    def __init__(self):
        self.cloth = cloth_mk002
        self.long_gun = None #当前只能装备一个
        self.short_gun = glock17 #当前只能装备一个
        self.grenade = []

        self.check_cloth_slot_correct()

        self.weight = self.cal_weight()
        self.long_gun_bullet_amount = self.cal_gun_bullet_amount(self.long_gun, "long_gun")
        self.short_gun_bullet_amount = self.cal_gun_bullet_amount(self.short_gun, "short_gun")




##############Instance####################
drill_outfit001 = DrillInfantryOutfit001()

if __name__ == '__main__':
    print drill_outfit001