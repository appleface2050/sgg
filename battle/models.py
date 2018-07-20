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
