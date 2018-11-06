#!/usr/bin/env python
#-*- coding:utf-8 -*-
"""
    author:commas
    datetime:2018/11/6 11:43
"""

from django.urls import path

from . import views

urlpatterns = [
    path('index/', views.index, name='index'),
    path('commas/', views.commas, name='commas'),
    path('blogs/', views.blogs, name='blogs'),
]