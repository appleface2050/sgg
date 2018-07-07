# coding=utf-8
from util.fun_ import get_current_accuracy_by_distance


def default_choose_weapon(main_weapon, subsidiary_weapon, target_distance):
    """
    选择武器
    """
    main_weapon_current_accuracy = get_current_accuracy_by_distance(main_weapon, target_distance)
    subsidiary_weapon_current_accuracy = get_current_accuracy_by_distance(subsidiary_weapon, target_distance)
    if main_weapon_current_accuracy >= subsidiary_weapon_current_accuracy:
        return main_weapon
    else:
        return subsidiary_weapon


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
    main_weapon_status = self_status.get("main_weapon_status")
    subsidiary_weapon_status = self_status.get("subsidiary_weapon_status")

    move = {"action_type": None, "target": None, "weapon": None}

    # if (not subsidiary_weapon and main_weapon.cartridge <= 0) or (
    #         main_weapon.cartridge <= 0 and subsidiary_weapon.cartridge <= 0):  # 没有副武器切主武器子弹用光 或 主武器副武器子弹用光
    #     move["action_type"] = "RETREAT"
    #     return move

    if main_weapon_status == "disable" and subsidiary_weapon_status == "disable":    #武器无法使用了
        move["action_type"] = "RETREAT"
        return move

    elif not target:  # 无目标，搜寻目标
        move["action_type"] = "SEARCHING"
        return move

    elif main_useful_weapon_best_shoot_distance < target_distance:  # 距离不足，接近敌人
        move["action_type"] = "APPROACHING"
        move["target"] = target
        return move

    else:  # 攻击
        # 选武器
        use_weapon = default_choose_weapon(main_weapon, subsidiary_weapon, target_distance)
        move = {"action_type": "ATTACKING", "target": target, "weapon": use_weapon}

    return move
