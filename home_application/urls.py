# -*- coding: utf-8 -*-
"""testapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url

from home_application import views

urlpatterns = (
    url(r'^$', views.home),
    url(r'^helloworld/$', views.hello_world),
    url(r'^sayhello/$', views.say_hello),
    url(r'^hostpage/', views.host_page),
    url(r'^hostdata/', views.host_data),

    url(r'^toolshome/', views.toolshome),
    url(r'^savetools/', views.savetools),
    url(r'^testtask/',views.testtask),
)
