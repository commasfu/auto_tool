#!/usr/bin/env python
#-*- coding:utf-8 -*-
"""
    author:commas
    datetime:2018/11/11 20:38
"""

from django import forms


class UserRegisterForm(forms.Form):
    username=forms.CharField(max_length=20,min_length=6,required=True,error_messages={
        'max_length':'用户名最大长度为20',
        'min_length':'用户名最小长度为6',
        'required':'用户名为必填'
    })
    email=forms.EmailField(max_length=100,min_length=8,required=False,error_messages={
        'invalid':'邮箱格式为:xxx@xx.com'
    })
    url=forms.URLField(max_length=100,min_length=8,required=False,error_messages={
        'invalid':'网址格式为:http://www.xxx.com'
    })
    password=forms.CharField(max_length=20,min_length=8,required=True,error_messages={
        'max_length':'密码最大长度为20',
        'min_length':'密码名最小长度为8',
        'required':'密码为必填'
    })
    password1=forms.CharField(max_length=20,min_length=8,required=True,error_messages={
        'max_length':'密码最大长度为20',
        'min_length':'密码名最小长度为8',
        'required':'密码为必填'
    })
class UserloginForm(forms.Form):
    username=forms.CharField(max_length=20,min_length=6,required=True)
    password=forms.CharField(max_length=20,min_length=8,required=True)