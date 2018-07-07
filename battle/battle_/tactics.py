# coding=utf-8


def default_tactics(self_status, team_status=None):
    """
    action_type: SEARCHING APPROACHING ATTACKING RETREAT
    target:
    weapon:
    """
    movement_ability = self_status.get("movement_ability")
    main_weapon = self_status.get("main_weapon")
    subsidiary_weapon = self_status.get("subsidiary_weapon")
    grenades = self_status.get("grenades")
    target = self_status.get("target")
    target_distance = self_status.get("target_distance")
    main_useful_weapon_best_shoot_distance = self_status.get("main_useful_weapon_best_shoot_distance")


    move = {"action_type": None, "target": None, "weapon": None}

    if (not subsidiary_weapon and main_weapon.cartridge <= 0) or (main_weapon.cartridge <= 0 and subsidiary_weapon.cartridge <= 0):  # 没有副武器切主武器子弹用光 或 主武器副武器子弹用光
        move["action_type"] = "RETREAT"
        return move

    elif not self_status["target"]:  # 无目标，搜寻目标
        move["action_type"] = "SEARCHING"
        return move

    elif self_status["target_distance"] > self_status["best_shoot_distance"]:  # 距离不足，接近敌人
        move["action_type"] = "APPROACHING"
        move["target"] = self_status["target"]
        return move

    else:  # 攻击
        move = {"action_type": "ATTACKING", "target": self_status["target"], "weapon": None}

    return move
