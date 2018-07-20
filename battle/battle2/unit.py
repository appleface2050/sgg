# coding=utf-8

class Unit(object):
    def __init__(self, name, belong):
        self.attack_accuracy = 30
        self.name = name
        self.belong = belong

    def __str__(self):
        return self.name

    def get_attack_accuracy(self):
        return self.attack_accuracy

    def get_belong(self):
        return self.belong

    def move(self):
        return self.attack()

    def attack(self):
        return "attack"