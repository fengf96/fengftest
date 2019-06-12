# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2019-06-12 19:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='HostModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name=b'\xe4\xb8\xbb\xe6\x9c\xba\xe5\x90\x8d')),
                ('ip', models.GenericIPAddressField(verbose_name=b'ip\xe5\x9c\xb0\xe5\x9d\x80')),
                ('system', models.CharField(choices=[(b'windows', b'windows'), (b'linux', b'linux'), (b'mac', b'mac')], max_length=30, verbose_name=b'\xe7\xb3\xbb\xe7\xbb\x9f')),
                ('disk_partition', models.CharField(max_length=100, verbose_name=b'\xe7\xa3\x81\xe7\x9b\x98\xe5\x88\x86\xe5\x8c\xba')),
                ('disk_capacity', models.FloatField(blank=True, null=True, verbose_name=b'\xe7\xa3\x81\xe7\x9b\x98\xe5\xae\xb9\xe9\x87\x8f(\xe5\x8d\x95\xe4\xbd\x8dGb)')),
                ('record_time', models.DateTimeField(auto_now=True, verbose_name=b'\xe5\x88\x9b\xe5\xbb\xba\xe6\x97\xb6\xe9\x97\xb4')),
            ],
            options={
                'verbose_name': '\u4e3b\u673a\u78c1\u76d8\u4fe1\u606f',
                'verbose_name_plural': '\u4e3b\u673a\u78c1\u76d8\u4fe1\u606f',
            },
        ),
        migrations.AlterUniqueTogether(
            name='hostmodel',
            unique_together=set([('ip', 'disk_partition')]),
        ),
    ]
