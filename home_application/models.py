# -*- coding: utf-8 -*-
# from django.db import models
# python manage.py makemigrations home_application
# python manage.py migrate home_application
# Create your models here.
from django.db import models


class HostModelManager(models.Manager):
    def to_dict(self):
        qs = super().get_queryset()
        res_dict = [{
            'host_name': item.name,
            'host_ip': item.ip,
            'host_system': item.system,
            'host_partition': item.disk_partition,
            'create_time': item.record_time.strftime("%y-%m-%d %H:%M:%S")
        } for item in qs]
        return res_dict


class HostModel(models.Model):
    SYSTEM_CHOICES = (
        ('windows', 'windows'),
        ('linux', 'linux'),
        ('mac', 'mac'),
    )
    name = models.CharField(max_length=30, verbose_name='主机名')
    ip = models.GenericIPAddressField(verbose_name='ip地址')
    system = models.CharField(choices=SYSTEM_CHOICES, max_length=30, verbose_name='系统')
    disk_partition = models.CharField(max_length=100, verbose_name='磁盘分区')
    disk_capacity = models.FloatField(blank=True, null=True, verbose_name='磁盘容量(单位Gb)')
    record_time = models.DateTimeField(auto_now=True, verbose_name='创建时间')

    objects = HostModelManager()

    class Meta:
        verbose_name = verbose_name_plural = '主机磁盘信息'
        unique_together = ('ip', 'disk_partition')


class ToolsModelManager(models.Manager):
    def to_dict(self):
        qs = super().get_queryset()
        res_dict = [{
            'toolname': item.toolname,
            'toolpath': item.toolpath,
            'toolclass': item.toolclass,
            'toolcapacity': item.toolcapacity,
            'recordtime': item.record_time.strftime("%y-%m-%d %H:%M:%S")
        } for item in qs]
        return res_dict


class ToolsModel(models.Model):
    CLASS_CHOICES = (
        ('windows', 'windows'),
        ('linux', 'linux'),
        ('mac', 'mac'),
    )
    toolname = models.CharField(max_length=128, verbose_name='工具名')
    toolpath = models.CharField(max_length=128,verbose_name='工具地址')
    toolclass = models.CharField(choices=CLASS_CHOICES, max_length=30, verbose_name='类别')
    toolcapacity = models.FloatField(blank=True, null=True, verbose_name='工具(单位Gb)')
    recordtime = models.DateTimeField(auto_now=True, verbose_name='创建时间')

    objects = ToolsModelManager()

    class Meta:
        verbose_name = verbose_name_plural = '工具信息'
