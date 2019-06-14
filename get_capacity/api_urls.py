# -*- coding: utf-8 -*-
from django.conf.urls import url

from get_capacity import api_views

# 提供磁盘容量历史数据查询API
urlpatterns = (
    url(r'^history_data/$', api_views.get_history_data),
)