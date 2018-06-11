# coding=utf-8
from util.baseclass import Gear


class Firearms(Gear):
    """
    枪械
    """
    class Meta:
        abstract = True

    def __init__(self):
        self.name = ""
        self.accuracy_15 = 0.0 #15m 以内射击精度
        self.accuracy_25 = 0.0
        self.accuracy_50 = 0.0
        self.accuracy_100 = 0.0
        self.accuracy_200 = 0.0
        self.accuracy_above_200 = 0.0 #200m以外射击精度
        self.mount_type = None #挂载类型
        self.weight = 0.0     #KG
        self.shoot_speed = 0 #每回合发射子弹数量
        self.cartridge_capacity = 0 #弹夹容量
        # self.bullet_type = ""

    def get_cartridge_capacity(self):
        return self.cartridge_capacity


class Pistol(Firearms):
    """
    手枪
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
        self.mount_type = "short_gun" #挂载类型 [short_gun, long_gun]
        self.shoot_speed = 6  # 每回合发射子弹数量

        self.name = "手枪"
        self.weight = 0.0
        self.cartridge_capacity = 0 #弹夹容量


class GlockG17(Pistol):
    def __init__(self):
        super(GlockG17, self).__init__()
        self.name = "GlockG17"
        self.weight = 1.1
        self.cartridge_capacity = 17 #弹夹容量




#############INSTANCE##################
glock17 = GlockG17()


if __name__ == '__main__':
    print glock17.accuracy_50





