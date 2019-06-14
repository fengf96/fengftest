# -*- coding: utf-8 -*-
"""
celery 任务

本地启动celery命令: python  manage.py  celery  worker  --settings=settings
周期性任务还需要启动celery调度命令：python  manage.py  celerybeat --settings=settings
"""
import datetime
import time

from celery import task, chain
from celery.schedules import crontab
from celery.task import periodic_task

from common.log import logger
from blueking.component.shortcuts import get_client_by_user
from get_capacity.utils import get_job_instance_id, get_host_capaticy


@task()
def async_task(username):
    """
    定义一个 celery 异步任务
    """
    # 执行Job作业，并获取磁盘容量信息写入库
    save_capacity_data(username)
    logger.error(u"save capacity celery任务执行成功")


@periodic_task(run_every=crontab(minute='*/1', hour='*', day_of_week="*"))
def save_capacity_data_periodic():
    """
    celery 周期任务示例
    
    run_every=crontab(minute='*/1', hour='*', day_of_week="*")：每 1 分钟执行一次任务
    periodic_task：程序运行时自动触发周期任务
    """
    save_capacity_data()
    now = datetime.datetime.now()
    logger.error(u"save capacity celery 周期任务调用成功，当前时间：{}".format(now))


def save_capacity_data(username='admin'):
    """
    执行 celery 异步任务

    调用celery任务方法:
        task.delay(arg1, arg2, kwarg1='x', kwarg2='y')
        task.apply_async(args=[arg1, arg2], kwargs={'kwarg1': 'x', 'kwarg2': 'y'})
        delay(): 简便方法，类似调用普通函数
        apply_async(): 设置celery的额外执行选项时必须使用该方法，如定时（eta）等
                      详见 ：http://celery.readthedocs.org/en/latest/userguide/calling.html
    """
    biz_id = 0              # 请修改为你需要执行的业务ID(可在蓝鲸配置平台里查询)
    ip = ''                 # 请修改为你需要执行的业务IP(可在蓝鲸配置平台里查询)
    job_id = 0              # 请修改为你需要执行的作业ID(可在蓝鲸作业平台里查询)

    alllogs = []
    ## 使用该方式调用云API时，请先将您的SaaS APPID 加入白名单 http://xx.xx.xx.xx/admin/bkcore/functioncontroller/
    client = get_client_by_user(username)
    result, job_instance_id = get_job_instance_id(client, biz_id, ip, job_id)
    while True:
        is_finish, capacity_data = get_host_capaticy(client, biz_id, job_instance_id, ip)
        if is_finish:
           break


## celery执行串行任务示例
@task()
def custom_func1(**kwargs):
    """
    @summary: 自定义函数1，可以自定义自己的逻辑处理
    """
    # 获取参数
    param1 = kwargs.get('param1', '')
    # 处理逻辑
    message = u"自定义函数——参数1为：%s" % (param1)
    # 休眠2秒
    time.sleep(2)
    taskid = datetime.datetime.now()
    # 返回参数
    ret_msg = {
        'param1': param1,
        'message': message,
        'taskid': taskid,
    }
    logger.error('custom_func1 result: %s' % ret_msg)
    return {'ret_msg': ret_msg}


@task()
def custom_func2(func_info, **kwargs):
    """
    @summary: 自定义函数2，可以自定义自己的逻辑处理
    """
    # 获取参数
    param2 = kwargs.get('param2', '')
    # 处理逻辑
    message = u"自定义函数——参数2为：%s" % (param2)
    # 休眠2秒
    time.sleep(2)
    ret_msg = {
        'param2': param2,
        'message': message,
        'prew_step_result': func_info
    }
    logger.error('custom_func2 result: %s' % ret_msg)
    return {'ret_msg': ret_msg}


@task()
def custom_func3(func_info, **kwargs):
    """
    @summary: 自定义函数3，可以自定义自己的逻辑处理
    """
    # 获取参数
    param3 = kwargs.get('param3', '')
    # 处理逻辑
    message = u"自定义函数——参数3为：%s" % (param3)
    # 休眠5秒
    time.sleep(5)
    ret_msg = {
        'param3': param3,
        'message': message,
        'prew_step_result': func_info
    }
    logger.error('custom_func3 result: %s' % ret_msg)
    return {'ret_msg': ret_msg}


@task()
def chain_task(func1_param, func2_param, func3_param):
    """
    串行任务
    """
    logger.error('chain_task %s, %s, %s' % (func1_param, func2_param, func3_param))
    chain(
        custom_func1.s(**func1_param),
        custom_func2.s(**func2_param),
        custom_func3.s(**func3_param),
    ).delay()


def celery_chain_task(params):
    """
    @summary: celery串行执行任务
    @note:
    后台任务：chain_task.delay(参数)
    后台定时任务：chain_task.apply_async((参数), eta=定时时间)
    调用celery任务方法详见 ：http://celery.readthedocs.org/en/latest/userguide/calling.html
    """
    print('celery_chain_task: %s' % params)
    func1_param = params.get('custom_func1', {})
    func2_param = params.get('custom_func2', {})
    func3_param = params.get('custom_func3', {}) 
    # 将任务串行起来，前面任务的返回可以作为后一个任务的参数
    chain_task.delay(func1_param, func2_param, func3_param)
    return (True, u"任务创建成功，正在后台执行")
