# coding=utf-8

class WeaponPackageSim001(object):
    def __init__(self):
        self.name = "模拟001"

        self.accuracy_15 = 0.60  # 15m 以内射击精度
        self.accuracy_25 = 0.30
        self.accuracy_50 = 0.05
        self.accuracy_100 = 0.0
        self.accuracy_200 = 0.0
        self.accuracy_above_200 = 0.0  # 200m以外射击精度

        self.shoot_speed = 6  # 每回合发射子弹数量

        self.cartridge = 120  # 子弹数量

        self.best_shoot_distance = 25


