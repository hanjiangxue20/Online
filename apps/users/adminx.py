#!/usr/bin/python3
# -*- coding: UTF-8 -*-
# Author:Chengnian  2038770992@qq.com

import xadmin
from xadmin import views

from .models import EmailVerifyRecord, Banner


# xadmin中这里是继承object  不再是admin
class EmailVerifyRecordAdmin(object):
    list_display = ['code', 'email', 'send_type', 'send_time']
    search_fields = ['code', 'email', 'send_type']
    list_filter = ['code', 'email', 'send_type', 'send_time']


class BannerAdmin(object):
    list_display = ['title', 'image', 'url', 'index', 'add_time']
    search_fields = ['title', 'image', 'url', 'index', ]
    list_filter = ['title', 'image', 'url', 'index', 'add_time']


# 创建xadmin的最基本管理器配置，并与view绑定
class BaseSetting(object):
    # 开启主题功能
    enable_themes = True
    use_bootswatch = True


# 全局修改，固定写法
class GlobalSetting(object):
    # 修改title
    site_title = "在线学习平台"
    # 修改footer
    site_footer = 'zkca'
    # 收起菜单
    menu_style = 'accordion'


xadmin.site.register(EmailVerifyRecord, EmailVerifyRecordAdmin)
xadmin.site.register(Banner, BannerAdmin)

# 将基本配置管理与view绑定
xadmin.site.register(views.BaseAdminView, BaseSetting)
# 将title和footer信息进行注册
xadmin.site.register(views.CommAdminView, GlobalSetting)
