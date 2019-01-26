#!/usr/bin/python3
# -*-coding:utf-8-*-
# Author: chengnian_20@163.com    in 2019
from django.urls import path, re_path
from organization.views import OrgView, TeacherView

app_name = "organization"

urlpatterns = [
    path('list/', OrgView.as_view(), name='org_list'),

    path('teacher/list/', TeacherView.as_view(), name='teacher_list'),

]
