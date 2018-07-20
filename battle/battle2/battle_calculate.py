# coding=utf-8
import random

def hit(accuracy):
    return accuracy > random.randint(0, 99)

def shuffle(lis):
    for i in range(len(lis) - 1, 0, -1):
        p = random.randrange(0, i + 1)
        lis[i], lis[p] = lis[p], lis[i]
    return lis