#coding=utf8
from django.db import models
from django.contrib.auth.models import AbstractBaseUser , BaseUserManager
from django.contrib import admin
from utils.base import BaseModelManager

class CaseManager(BaseModelManager):
    pass

class Case(models.Model):
    class Meta:
        verbose_name_plural = u'案例'
        ordering = ['-date']
        
    date = models.DateTimeField('更新日期',auto_now_add=True)
    name = models.CharField('主旨标题',max_length=256)
    content = models.TextField('更新内容')
    img = models.ImageField('展示图片',upload_to='case')
    
    objects = CaseManager()
    
    def __unicode__(self):
        return self.content


class CaseAdmin(admin.ModelAdmin):
    list_display = ('date','name','content','img')
    

admin.site.register(Case, CaseAdmin)