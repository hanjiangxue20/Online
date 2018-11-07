#!/usr/bin/python3
# -*- coding: UTF-8 -*-
# Author:Chengnian  2038770992@qq.com

import xadmin

from .models import UserAsk, UserMessage, CourseComments, UserCourse, UserFavorite


class UserAskAdmin(object):
    """
    用户表单我要学习'
    """
    list_display = ['name', 'mobile', 'course_name', 'add_time']
    search_fields = ['name', 'mobile', 'course_name']
    list_filter = ['name', 'mobile', 'course_name', 'add_time']


class UserCourseAdmin(object):
    """
    用户课程学习
    """
    list_display = ['course', 'course', 'add_time']
    search_fields = ['course', 'course']
    list_filter = ['course', 'course', 'add_time']


class UserMessageAdmin(object):
    list_display = ['user', 'message', 'has_red', 'add_time']
    search_fields = ['user', 'message', 'has_red']
    list_filter = ['user', 'message', 'has_red', 'add_time']


class CourseCommentsAdmin(object):
    '''用户评论后台'''

    list_display = ['user', 'course', 'comments', 'add_time']
    search_fields = ['user', 'course', 'comments']
    list_filter = ['user', 'course', 'comments', 'add_time']


class UserFavoriteAdmin(object):
    '''用户收藏后台'''

    list_display = ['user', 'fav_id', 'fav_type', 'add_time']
    search_fields = ['user', 'fav_id', 'fav_type']
    list_filter = ['user', 'fav_id', 'fav_type', 'add_time']


xadmin.site.register(UserAsk, UserAskAdmin)
xadmin.site.register(UserCourse, UserCourseAdmin)
xadmin.site.register(UserMessage, UserMessageAdmin)
xadmin.site.register(CourseComments, CourseCommentsAdmin)
xadmin.site.register(UserFavorite, UserFavoriteAdmin)
