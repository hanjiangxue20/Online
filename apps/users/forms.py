#!/usr/bin/python3
# -*-coding:utf-8-*-
# Author: chengnian_20@163.com    in 2018

from django import forms
from captcha.fields import CaptchaField


# 登录表单验证
class LoginForm(forms.Form):
    # 用户名密码不能为空
    username = forms.CharField(required=True)
    password = forms.CharField(required=True, min_length=5)


class RegisterForm(forms.Form):
    '''注册表单验证'''
    email = forms.EmailField(required=True)
    password = forms.CharField(required=True,min_length=5)
    #验证码 字段里可以自定义错误提示
    captcha = CaptchaField(error_messages={'invalid':'验证码错误'})
