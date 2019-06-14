# -*- coding: utf-8 -*-
import datetime
import logging
import time
from celery import task
from celery.task import periodic_task

logger = logging.getLogger('celery')

@task()
def get_capacity_task():
    """
    定义一个获取磁盘使用率异步任务
    """
    logger.info('disk usage work end')


@periodic_task(run_every=datetime.timedelta(seconds=1))
def get_disk_periodic():
    """
    获取磁盘使用率周期执行定义
    """
    get_capacity_task.delay()
    logger.info('get disk work starting')

@task
def sayhello():
    print('hello ...')
    time.sleep(2)
    print('world ...')