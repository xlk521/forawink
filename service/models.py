#coding=utf8
from django.db import models
from django.contrib.auth.models import AbstractBaseUser , BaseUserManager
from django.contrib import admin
from utils.base import BaseModelManager

class ServiceDevelopmentManager(BaseModelManager):
    pass

class ServiceDevelopment(models.Model):
    class Meta:
        verbose_name_plural = u'应用软件开发'
        ordering = ['cls','date']
        
    SERVICE_CLS= (
        ('head', 'head:一组'),
        ('企业资源计划', '企业资源计划:一组'),
        ('移动商务应用', '移动商务应用:一组'),
        ('物联网及数据监测平台', '物联网及数据监测平台:一组'),
        ('数字化营销平台', '数字化营销平台:一组'),
    )
    date = models.DateTimeField('更新日期',auto_now_add=True)
    cls = models.CharField('类别',max_length=32,choices=SERVICE_CLS,default='head')
    name = models.CharField('标题',max_length=256)
    content = models.TextField('更新内容')
    img = models.ImageField('资源图片',upload_to='service')
    
    objects = ServiceDevelopmentManager()
    
    def __unicode__(self):
        return self.cls
    
class ServiceSupportManager(BaseModelManager):
    pass

class ServiceSupport(models.Model):
    class Meta:
        verbose_name_plural = u'信息技术支持'
        ordering = ['cls','date']
        
    SERVICE_CLS= (
        ('head', 'head:一组'),
        ('企业IT战略规划', '企业IT战略规划:一组'),
        ('企业IT系统架构设计', '企业IT系统架构设计:一组'),
        ('信息安全和系统保证', '信息安全和系统保证:一组'),
        ('敏捷精益软件开发方法', '敏捷精益软件开发方法:一组'),
    )
    date = models.DateTimeField('更新日期',auto_now_add=True)
    cls = models.CharField('类别',max_length=32,choices=SERVICE_CLS,default='head')
    name = models.CharField('标题',max_length=256)
    content = models.TextField('更新内容')
    img = models.ImageField('资源图片',upload_to='service')
    
    objects = ServiceSupportManager()
    
    def __unicode__(self):
        return self.cls

class ServiceUIManager(BaseModelManager):
    pass

class ServiceUI(models.Model):
    class Meta:
        verbose_name_plural = u'UI/VI设计'
        ordering = ['cls','date']
        
    SERVICE_CLS= (
        ('head', 'head:一组'),
        ('UI设计', 'UI设计:一组'),
        ('移动界面设计', '移动界面设计:一组'),
        ('网站开发', '网站开发:一组'),
    )
    date = models.DateTimeField('更新日期',auto_now_add=True)
    cls = models.CharField('类别',max_length=32,choices=SERVICE_CLS,default='head')
    name = models.CharField('标题',max_length=256)
    content = models.TextField('更新内容')
    img = models.ImageField('资源图片',upload_to='service')
    
    objects = ServiceSupportManager()
    
    def __unicode__(self):
        return self.cls
    
class ServiceDevelopmentAdmin(admin.ModelAdmin):
    list_display = ('cls','content','img')
class ServiceSupportAdmin(admin.ModelAdmin):
    list_display = ('cls','content','img')
class ServiceUIAdmin(admin.ModelAdmin):
    list_display = ('cls','content','img')
    

admin.site.register(ServiceDevelopment, ServiceDevelopmentAdmin)
admin.site.register(ServiceSupport, ServiceSupportAdmin)
admin.site.register(ServiceUI, ServiceUIAdmin)