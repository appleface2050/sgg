# coding=utf-8

import datetime
from battle_sim.infantry_outfit import drill_outfit001


class InfantrySoldier(object):
    """
    士兵
    """

    # def __init__(self):
    #     self.out_fit = drill_outfit001
    #     self.weight = self.out_fit.get_weight()

    def __init__(self, outfit):
        self.out_fit = outfit
        self.weight = self.out_fit.get_weight()

    def __str__(self):
        outfit_d = "outfit: " + self.out_fit.cloth.name + "\n"
        long_gun_d = "long gun: " + self.out_fit.long_gun.name + "\n"
        short_gun_d = "short gun: " + self.out_fit.short_gun.name + "\n"
        grenade_d = "grenade: " + str(self.out_fit.grenade) + "\n"
        long_gun_bullet_amount_d = "long gun bullet amount: " + str(self.out_fit.long_gun_bullet_amount) + "\n"
        short_gun_bullet_amount_d = "short gun bullet amount: " + str(self.out_fit.short_gun_bullet_amount) + "\n"
        weight_d = "weight: " + str(self.out_fit.weight) + "\n"

        desc = outfit_d + long_gun_d + short_gun_d + grenade_d + weight_d + long_gun_bullet_amount_d + short_gun_bullet_amount_d
        return desc


if __name__ == '__main__':
    now = datetime.datetime.now()
    a = InfantrySoldier(drill_outfit001)
    print a.weight
    print datetime.datetime.now() - now
