# -*- coding: utf-8 -*-


from django.conf.urls import url

from get_capacity import views

urlpatterns = (
    url(r'^', views.home),
    # 表单下拉数据获取及渲染
    url(r'^get_biz_list/$', views.get_biz_list),
    url(r'^get_ip_by_bizid/$', views.get_ip_by_bizid),
    url(r'^get_job_list/$', views.get_joblist_by_bizid),

    # 执行作业，获取容量数据
    url(r'^execute_job/$', views.execute_job),
    url(r'^get_capacity/$', views.get_capacity),

    # 获取视图数据
    url(r'^chartdata/$', views.get_capacity_chartdata)
)