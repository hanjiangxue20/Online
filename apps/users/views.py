from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.db.models import Q
from .models import UserProfile
from django.contrib.auth.backends import ModelBackend


# Create your views here.

def user_login(request):
    if request.method == "POST":
        # 获取用户提交数据
        user_name = request.POST.get('username', None)
        pass_word = request.POST.get('password', None)
        # 成功返回user对象，失败None
        user = authenticate(username=user_name, password=pass_word)
        # 如果不是null说明验证成功
        if user is not None:
            # 登录
            login(request, user)
            return render(request, 'index.html')
        else:
            return render(request, 'login.html', {'msg': '用户或者密码错误'})
    elif request.method == 'GET':
        return render(request, 'login.html')


# 邮箱和用户名都可以登录
class CustomBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            # 不希望用户存在两个，get只能有一个。两个是get失败的一种原因 Q为使用并集查询
            user = UserProfile.objects.get(Q(username=username) | Q(email=username))
            # django的后台中密码加密：所以不能password==password
            # UserProfile继承的AbstractUser中有def check_password(self, raw_password):
            if user.check_password(password):
                return user
        except Exception as e:
            return None
