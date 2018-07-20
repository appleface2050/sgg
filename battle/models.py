# coding=utf-8

from __future__ import unicode_literals

from django.db import models

# Create your models here.
from util.baseclass import JSONBaseModel


class Battle(JSONBaseModel):
    """
    战斗
    """
    start_date = models.DateField(null=False, verbose_name=u'日期', db_index=True)
    home = models.CharField(max_length=254, unique=False, null=False, blank=False, db_index=True)
    away = models.CharField(max_length=254, unique=False, null=False, blank=False, db_index=True)
    winner = models.CharField(max_length=254, unique=False, null=False, blank=False, db_index=True)
    home_casualties = models.CharField(max_length=8192, unique=False, null=False, blank=False)
    away_casualties = models.CharField(max_length=8192, unique=False, null=False, blank=False)
    uptime = models.DateTimeField(auto_now=True, verbose_name=u'数据更新时间')

    @classmethod
    def add_data(cls, start_date, home, away, winner, home_casualties, away_casualties):
        a = cls()
        a.start_date = start_date
        a.home = home
        a.away = away
        a.winner = winner
        a.home_casualties = home_casualties
        a.away_casualties = away_casualties
        a.save()

class BattleProcess(JSONBaseModel):
    """
    战斗进程
    """
    battle_id = models.IntegerField(default=0, null=False, db_index=True)
    round = models.IntegerField(default=0, null=False)
    belong = models.CharField(max_length=32, unique=False, null=False, blank=False)
    unit = models.CharField(max_length=64, unique=False, null=False, blank=False)
    target = models.CharField(max_length=64, unique=False, null=False, blank=False)
    move = models.CharField(max_length=64, unique=False, null=False, blank=False)
    result = models.CharField(max_length=64, unique=False, null=False, blank=False)
    uptime = models.DateTimeField(auto_now=True, verbose_name=u'数据更新时间')

    @classmethod
    def add_data(cls, battle_id, belong, unit, target, move, result):
        a = cls()
        a.battle_id = battle_id
        a.belong = belong
        a.unit = unit
        a.target = target
        a.move = move
        a.result = result
        a.save()
