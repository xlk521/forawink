#coding=utf8
from django.db import models
from django.contrib.auth.models import AbstractBaseUser , BaseUserManager
from django.contrib import admin
from utils.base import BaseModelManager

class HomeImgManager(BaseModelManager):
    pass

class HomeImg(models.Model):
    class Meta:
        verbose_name_plural = u'轮播图片资源：多组'
        
    date = models.DateTimeField('更新日期',auto_now_add=True)
    content = models.TextField('更新内容')
    img = models.ImageField('图片资源',upload_to='home')
    
    objects = HomeImgManager()
    
    def __unicode__(self):
        return self.content


class HomeUsingImgManager(BaseModelManager):
    pass

class HomeUsingImg(models.Model):
    class Meta:
        verbose_name_plural = u'应用软件开发：一组'
        
    date = models.DateTimeField('更新日期',auto_now_add=True)
    img = models.ImageField('图片资源',upload_to='home')
    
    objects = HomeUsingImgManager()
    
class HomeTechnologyImgManager(BaseModelManager):
    pass

class HomeTechnologyImg(models.Model):
    class Meta:
        verbose_name_plural = u'信息技术支持：一组'
        
    date = models.DateTimeField('更新日期',auto_now_add=True)
    img = models.ImageField('图片资源',upload_to='home')
    
    objects = HomeTechnologyImgManager()
    
class HomeUIImgManager(BaseModelManager):
    pass

class HomeUIImg(models.Model):
    class Meta:
        verbose_name_plural = u'UI/VI：一组'
        
    date = models.DateTimeField('更新日期',auto_now_add=True)
    img = models.ImageField('图片资源',upload_to='home')
    
    objects = HomeUIImgManager()
    
class HomeCaseImgManager(BaseModelManager):
    pass

class HomeCaseImg(models.Model):
    class Meta:
        verbose_name_plural = u'案例:多组'
        
    date = models.DateTimeField('更新日期',auto_now_add=True)
    img = models.ImageField('图片资源',upload_to='home')
    url = models.URLField('页面链接')
    content = models.TextField('案例简述')
    
    objects = HomeCaseImgManager()
    
    def __unicode__(self):
        return self.content
    
class HomeImgAdmin(admin.ModelAdmin):
    list_display = ('date','content','img')
    
class HomeUsingImgAdmin(admin.ModelAdmin):
    list_display = ('date','img')
    
class HomeTechnologyImgAdmin(admin.ModelAdmin):
    list_display = ('date','img')
    
class HomeUIImgAdmin(admin.ModelAdmin):
    list_display = ('date','img')
    
class HomeCaseImgAdmin(admin.ModelAdmin):
    list_display = ('date','img')
    
admin.site.register(HomeImg, HomeImgAdmin)
admin.site.register(HomeUsingImg, HomeUsingImgAdmin)
admin.site.register(HomeTechnologyImg, HomeTechnologyImgAdmin)
admin.site.register(HomeUIImg, HomeUIImgAdmin)
admin.site.register(HomeCaseImg, HomeCaseImgAdmin)