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
