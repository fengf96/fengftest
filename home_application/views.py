# -*- coding: utf-8 -*-
import re
import time

from django.shortcuts import render

from home_application import  celery_tasks
from home_application.models import HostModel
from my_common.utils import render_json

# 开发框架中通过中间件默认是需要登录态的，如有不需要登录的，可添加装饰器login_exempt
# 装饰器引入 from blueapps.account.decorators import login_exempt
def home(request):
    """
    首页
    """
    return render(request, 'home_application/home.html')

def hello_world(request):
    """
    作业二主页
    """
    return render(request, 'home_application/helloworld.html')

def testtask(request):
    celery_tasks.sayhello.delay()
    return render_json("hello")
def say_hello(request):
    """
    作业二后端逻辑验证
    """
    # print("hello.....")
    # time.sleep(2)
    # print("hello.....")
    # celery_tasks.get_capacity_task()

    data = request.POST.get('input', None)
    data = 'Congratulations!\n'+data
    res = {'data': data}
    return render_json(res)


def host_page(request):
    """
    作业三主页
    """
    return render(request, 'home_application/hostpage.html')


def host_data(request):
    """
    作业三数据提交与获取
    """
    if request.method == 'POST':
        host_name = request.POST.get('hostname', None)
        host_ip = request.POST.get('ip', None)
        host_system = request.POST.get('system', None)
        host_partition = request.POST.get('partition', None)

        if "" in [host_name, host_ip, host_system, host_partition]:
            return render_json({'code': -1, 'msg': 'some of params lost.'})
        if re.match('(\d{1,3}\.){3}\d{1,3}', host_ip) is None:
            return render_json({'code': -1, 'msg': 'wrong ip format.'})

        try:
            HostModel.objects.create(name=host_name, ip=host_ip, system=host_system, disk_partition=host_partition)
        except Exception as e:
            return render_json({'code': -1, 'msg': 'exists same host_ip and host_partition pair.'})

        return render_json({'code': 0, 'msg': 'data insert success.'})
    else:
        return render_json({'code': 0, 'items': HostModel.objects.to_dict(),
                            'catalogues': {
                                'host_name': '主机名',
                                'host_ip': '主机IP',
                                'host_system': '主机系统',
                                'host_partition': '磁盘分区',
                                'create_time': '创建时间',
                            }})

def toolshome(request):

    return render(request, 'home_application/toolshome.html')

def savetools(request):

    # if request.method == 'POST':
    #     toolname = request.POST.get('toolname', None)
    #     toolclass = request.POST.get('toolclass', None)
    #
    #     if "" in [host_name, host_ip, host_system, host_partition]:
    #         return render_json({'code': -1, 'msg': 'some of params lost.'})
    #     if re.match('(\d{1,3}\.){3}\d{1,3}', host_ip) is None:
    #         return render_json({'code': -1, 'msg': 'wrong ip format.'})
    #
    #     try:
    #         HostModel.objects.create(name=host_name, ip=host_ip, system=host_system, disk_partition=host_partition)
    #     except Exception as e:
    #         return render_json({'code': -1, 'msg': 'exists same host_ip and host_partition pair.'})
    #
    #     return render_json({'code': 0, 'msg': 'data insert success.'})
    # else:
    #     return render_json({'code': 0, 'items': HostModel.objects.to_dict(),
    #                         'catalogues': {
    #                             'host_name': '主机名',
    #                             'host_ip': '主机IP',
    #                             'host_system': '主机系统',
    #                             'host_partition': '磁盘分区',
    #                             'create_time': '创建时间',
    #                         }})
    pass
