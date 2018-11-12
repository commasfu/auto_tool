#!/usr/bin/env python
#-*- coding:utf-8 -*-
"""
    author:commas
    datetime:2018/11/11 20:46
"""

"""blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from apps.articles.views import article_detail,comment_add,love_add,article_add
app_name ='[app_name]'
urlpatterns = [
    url(r'^article_detail/(\d+)/$',article_detail,name='article_detail'),
    url(r'^article_add/$', article_add, name='article_add'),
    url(r'^comment_add/(\d+)/$',comment_add,name='comment_add'),
    url(r'^love_add/(\d+)/$', love_add, name='love_add'),
]