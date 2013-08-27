#coding=utf8
from django.db import models
from django.contrib.auth.models import AbstractBaseUser , BaseUserManager
from django.contrib import admin
from utils.base import BaseModelManager

class AboutManager(BaseModelManager):
    pass

class About(models.Model):
    class Meta:
        verbose_name_plural = u'关于本网站'
        ordering = ['-date']

    COMPANYINTRODUCTION = '公司简介'
    BUSINESSPHILOSOPHY = '经营理念'
    CONTACTUS = '联系我们'
    CHOICES = (
        (COMPANYINTRODUCTION, '公司简介:一组'),
        (BUSINESSPHILOSOPHY, '经营理念:一组'),
        (CONTACTUS, '联系我们:一组'),
    )
    date = models.DateTimeField('更新日期',auto_now_add=True)
    cls = models.CharField('主旨标题',max_length=32,choices=CHOICES,default=COMPANYINTRODUCTION)
    content = models.TextField('更新内容')
    img = models.ImageField('展示图片',upload_to='about')
    purport = models.CharField('主旨标题',max_length=256)
    
    objects = AboutManager()
    
    def __unicode__(self):
        return self.purport

class AboutAdmin(admin.ModelAdmin):
    list_display = ('date','cls','content')
    
admin.site.register(About, AboutAdmin)