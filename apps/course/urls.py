#!/usr/bin/python3
# -*-coding:utf-8-*-
# Author: chengnian_20@163.com    in 2019
from django.urls import path

from course.views import CourseListView

app_name = 'course'

urlpatterns = [
    path('list/', CourseListView.as_view(), name='course_list'),

]
