"""Online URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path, include, re_path
from django.views.generic import TemplateView
from Online.settings import MEDIA_ROOT
from django.views.static import serve

from users.views import LoginView,LogoutView, RegisterView, ForgetPwdView, ActiveUserView, ResetView, ModifyPwdView
import xadmin

app_name = 'online'

urlpatterns = [
    path('xadmin/', xadmin.site.urls),
    path('', TemplateView.as_view(template_name='index.html'), name='index'),
    # path('login/', views.user_login, name='login'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', RegisterView.as_view(), name='register'),
    path('captcha/', include('captcha.urls')),
    path('forget/', ForgetPwdView.as_view(), name='forget_pwd'),
    re_path('active/(?P<active_code>.*)/', ActiveUserView.as_view(), name='user_active'),
    re_path('reset/(?P<active_code>.*)/', ResetView.as_view(), name='reset_pwd'),
    path('modify_pwd/', ModifyPwdView.as_view(), name='modify_pwd'),
    # 课程机构app相关url配置
    path('org/', include('organization.urls', namespace='org')),
    # 课程app相关url配置
    path('course/', include('course.urls', namespace='course')),
    # 个人信息
    path('users/', include('users.urls', namespace='users')),
    # 静态文件
    # re_path(r'^static/(?P<path>.*)', serve, {"document_root": STATICFILES_DIRS }),
    # 富文本
    # path('ueditor/',include('')),
    # 处理图片显示的url,使用Django自带serve,传入参数告诉它去哪个路径找，我们有配置好的路径MEDIAROOT
    re_path(r'^media/(?P<path>.*)', serve, {"document_root": MEDIA_ROOT}),

]

# 全局404页面配置
# handler404 = 'users.views.pag_not_found'
# 全局500页面配置
# handler500 = 'users.views.page_error'
