from django.db import models
from django.contrib.auth.models import AbstractUser
from datetime import datetime
# Create your models here.
class UserProfile(AbstractUser):
    nick_name=models.CharField(max_length=20,verbose_name='用户昵称',null=True,blank=True)
    url=models.URLField(max_length=100,verbose_name='用户主页',null=True,blank=True)
    add_time=models.DateTimeField(default=datetime.now,verbose_name='添加时间')

    def __str__(self):
        return self.username

    class Meta:
        verbose_name='用户信息'
        verbose_name_plural=verbose_name