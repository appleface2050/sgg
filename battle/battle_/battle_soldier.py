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

    def packet_status(self):
        return {"name": self.name, "weight": self.weight, "movement_ability": self.movement_ability,
                "grenades": self.grenades,
                "main_weapon": self.main_weapon, "subsidiary_weapon": self.subsidiary_weapon,
                "target": self.target, "target_distance": self.target_distance,
                "main_useful_weapon_best_shoot_distance": self.main_useful_weapon_best_shoot_distance}

    def make_move(self):
        status = self.packet_status()
        move = self.tactics(status)
        return move

    def update_main_useful_weapon_best_shoot_distance(self):
        if self.main_weapon.cartridge > 0:
            return self.main_weapon.best_shoot_distance
        elif self.subsidiary_weapon and self.subsidiary_weapon > 0:
            return self.subsidiary_weapon.best_shoot_distance
        else:
            return None

    def do_update(self):
        self.main_useful_weapon_best_shoot_distance = self.update_main_useful_weapon_best_shoot_distance()
