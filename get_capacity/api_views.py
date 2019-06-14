# -*- coding: utf-8 -*-

import json
import datetime
from common.mymako import render_mako_context, render_json
from account.decorators import login_exempt
from get_capacity.models import CapacityData

TOKEN = '@adf*adsd^'

@login_exempt
def get_history_data(request):
    """
    获取磁盘容量历史数据 API
    """
    # print("获取磁盘容量历史数据 API")
    ip = request.GET.get('ip', '')
    filesystem = request.GET.get('filesystem', '')
    mounted = request.GET.get('mounted', '')
    token = request.GET.get('token', '')
    if token != TOKEN:
        return render_json({'result': False, 'data': [], 'message': u"token不合法"})

    capacitydatas = CapacityData.objects.all()
    if ip:
        capacitydatas = capacitydatas.filter(ip=ip)
    if filesystem:
        capacitydatas = capacitydatas.filter(filesystem=filesystem)
    if mounted:
        capacitydatas = capacitydatas.filter(mounted=mounted)

    datalist = []
    for _data in capacitydatas:
        datalist.append(
            {
                'ip': _data.ip,
                'filesystem': _data.filesystem,
                'mounted': _data.mounted,
                'size': _data.size,
                'use': _data.use,
                'createtime': _data.createtime.strftime('%Y-%m-%d %H:%M:%S')
            }
        )
    
    return render_json({'result': True, 'data': datalist, 'message': 'ok'})