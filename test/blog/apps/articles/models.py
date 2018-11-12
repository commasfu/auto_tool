from django.db import models

# Create your models here.

import os
import sys

base_path = os.path.dirname(os.path.dirname(__file__))
sys.path.append(base_path)
print(base_path)

from django.db import models
from datetime import datetime
from apps.user.models import UserProfile
# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=20,verbose_name="文章类别")
    add_time = models.DateTimeField(default=datetime.now,verbose_name="添加时间")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "类别信息"
        verbose_name_plural = verbose_name

class ArticleInfo(models.Model):
    title = models.CharField(max_length=50,verbose_name="文章标题")
    author = models.ForeignKey(UserProfile,verbose_name='文章作者',on_delete=models.CASCADE)
    category = models.ForeignKey(Category,verbose_name="所属类别",null=True,blank=True,on_delete=models.CASCADE)
    desc = models.CharField(max_length=200,verbose_name="文章摘要")
    content = models.TextField(verbose_name="文章内容")
    is_delete = models.BooleanField(default=False,verbose_name="是否删除")
    click_num = models.IntegerField(default=0,verbose_name="浏览量")
    love_num = models.IntegerField(default=0,verbose_name="点赞数")
    image = models.ImageField(max_length=200,verbose_name="文章图片",upload_to='article/%y/%m/%d')
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = '文章信息'
        verbose_name_plural = verbose_name

class TagInfo(models.Model):
    name = models.CharField(max_length=20,verbose_name='标签名称')
    article = models.ManyToManyField(ArticleInfo,verbose_name="所属文章")
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "标签信息"
        verbose_name_plural = verbose_name

class CommentInfo(models.Model):
    comment_man = models.ForeignKey(UserProfile,verbose_name="评论人",on_delete=models.CASCADE)
    comment_art = models.ForeignKey(ArticleInfo,verbose_name="评论文章",on_delete=models.CASCADE)
    comment_content = models.TextField(verbose_name="评论内容")
    is_delete = models.BooleanField(default=False,verbose_name="是否删除")
    add_time = models.DateTimeField(default=datetime.now,verbose_name="评论时间")

    def __str__(self):
        return self.comment_content

    class Meta:
        verbose_name = "评论信息"
        verbose_name_plural = verbose_name