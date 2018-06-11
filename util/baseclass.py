# coding=utf-8

class Gear(object):
    """
    装备
    """
    class Meta:
        abstract = True

    def get_weight(self):
        return self.weight