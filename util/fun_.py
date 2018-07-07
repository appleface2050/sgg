import random


def shuffle(lis):
    for i in range(len(lis) - 1, 0, -1):
        p = random.randrange(0, i + 1)
        lis[i], lis[p] = lis[p], lis[i]
    return lis


def get_current_accuracy_by_distance(weapon, distance):
    if not weapon:
        return 0
    else:
        result = 0
        if distance <= weapon.accuracy_15:
            return weapon.accuracy_15
        elif distance <= weapon.accuracy_25:
            return weapon.accuracy_25
        elif distance <= weapon.accuracy_50:
            return weapon.accuracy_50
        elif distance <= weapon.accuracy_100:
            return weapon.accuracy_100
        elif distance <= weapon.accuracy_200:
            return weapon.accuracy_200
        elif distance <= weapon.accuracy_above_200:
            return weapon.accuracy_above_200
        else:
            raise Exception("get_current_accuracy_by_distance")

if __name__ == '__main__':
    print shuffle([1, 2, 3, 4, 5])
