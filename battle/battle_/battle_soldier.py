# coding=utf-8
from battle.battle_.tactics import default_tactics


class BattleSoldier(object):
    """
    士兵（已有装备）
    """

    def __init__(self, name, main_weapon_package, subsidiary_weapon_package=None, grenades=None,
                 tactics=default_tactics):
        assert main_weapon_package != None

        self.name = name
        self.weight = None

        # 每回合行动距离 m
        self.movement_ability = 5

        # 主武器

        self.main_weapon = main_weapon_package
        self.subsidiary_weapon = subsidiary_weapon_package
        self.grenades = grenades

        self.tactics = tactics

        # 战斗状态
        self.target = None
        self.target_distance = None
        self.main_useful_weapon_best_shoot_distance = self.update_main_useful_weapon_best_shoot_distance()
        self.main_weapon_status = "normal"
        self.subsidiary_weapon_status = self.update_weapon_status("subsidiary_weapon")

    def if_cartridge_not_empty(self, weapon_type):
        if weapon_type == "main_weapon":  # 主武器
            return self.main_weapon.cartridge > 0  # 有子弹
        elif weapon_type == "subsidiary_weapon":  # 副武器
            if self.subsidiary_weapon:  # 有副武器
                return self.subsidiary_weapon.cartridge > 0  # 有子弹
            else:
                return False
        else:
            assert Exception("if_cartridge_not_empty")

    def update_weapon_status(self, type):
        """
        更新武器状态
        """
        if type == "main_weapon":
            if self.if_cartridge_not_empty("main_weapon"):
                self.main_weapon_status = "normal"
            else:
                self.main_weapon_status = "disable"
        elif type == "subsidiary_weapon":
            if not self.subsidiary_weapon:
                self.subsidiary_weapon_status = "disable"
            elif self.if_cartridge_not_empty("subsidiary_weapon"):
                self.subsidiary_weapon_status = "normal"
            else:
                self.subsidiary_weapon_status = "disable"
        # elif type == "grenades":
        #     if self.grenades:
        #         return "normal"
        #     else:
        #         return "disable"

    def packet_status(self):
        return {"name": self.name, "weight": self.weight, "movement_ability": self.movement_ability,
                "grenades": self.grenades,
                "main_weapon": self.main_weapon, "subsidiary_weapon": self.subsidiary_weapon,
                "target": self.target, "target_distance": self.target_distance,
                "main_useful_weapon_best_shoot_distance": self.main_useful_weapon_best_shoot_distance,
                "main_weapon_status": self.main_weapon_status,
                "subsidiary_weapon_status": self.subsidiary_weapon_status}

    def make_move(self):
        status = self.packet_status()
        move = self.tactics(status)
        return move

    def update_main_useful_weapon_best_shoot_distance(self):
        """
        更新能用的武器的最佳射击距离
        """
        if self.main_weapon.cartridge > 0:
            return self.main_weapon.best_shoot_distance
        elif self.subsidiary_weapon and self.subsidiary_weapon > 0:
            return self.subsidiary_weapon.best_shoot_distance
        else:
            return None

    def do_update(self):
        self.update_weapon_status("main_weapon")
        self.update_weapon_status("subsidiary_weapon")
        self.main_useful_weapon_best_shoot_distance = self.update_main_useful_weapon_best_shoot_distance()
