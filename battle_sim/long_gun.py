# coding=utf-8
from battle_sim.firearms import Firearms


class LongGun(Firearms):
    """
    长枪
    """
    class Meta:
        abstract = True

    def __init__(self):
        self.accuracy_15 = 0.60 #15m 以内射击精度
        self.accuracy_25 = 0.30
        self.accuracy_50 = 0.05
        self.accuracy_100 = 0.0
        self.accuracy_200 = 0.0
        self.accuracy_above_200 = 0.0 #200m以外射击精度
        self.mount_type = "long_gun" #挂载类型 [short_gun, long_gun]
        self.shoot_speed = 6  # 每回合发射子弹数量

        self.name = "长枪"
        self.weight = 0.0
        self.cartridge_capacity = 0 #弹夹容量

class LongGunNone(LongGun):
    def __init__(self):
        super(LongGunNone, self).__init__()
        self.name = ""
        self.weight = 0.0
        self.cartridge_capacity = 0 #弹夹容量


long_gun_none = LongGunNone()