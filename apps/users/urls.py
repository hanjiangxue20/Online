#!/usr/bin/python3
# -*-coding:utf-8-*-
# Author: chengnian_20@163.com    in 2019
from django.urls import path

from users.views import UserinfoView

app_name = 'users'
urlpatterns = [
    # 用户信息
    path('info/', UserinfoView.as_view(), name='user_info'),
]
