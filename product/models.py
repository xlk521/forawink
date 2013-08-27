#coding=utf8
from django.db import models
from django.contrib.auth.models import AbstractBaseUser , BaseUserManager
from django.contrib import admin
from utils.base import BaseModelManager
from weike.settings import PRODUCTS_3 ,PRODUCTS_2 ,PART

class ProductCoordinationManager(BaseModelManager):
    pass

class ProductCoordination(models.Model):
    class Meta:
        verbose_name_plural = u'协同办公平台'
        ordering = ['cls','name','-date']
        
    date = models.DateTimeField('更新日期',auto_now_add=True)
    cls = models.CharField('类别',max_length=32,choices=PRODUCTS_3,default='概述')
    part = models.CharField('显示区域',max_length=32,choices=PART,default='part1')
    name = models.CharField('标题',max_length=256)
    purpore = models.CharField('小标题',max_length=256)
    content = models.TextField('更新内容')
    img = models.ImageField('资源图片',upload_to='product')
    
    objects = ProductCoordinationManager()
    
    def __unicode__(self):
        return self.name

class ProductResourceManager(BaseModelManager):
    pass

class ProductResource(models.Model):
    class Meta:
        verbose_name_plural = u'企业资源计划'
        ordering = ['cls','name','-date']
        
    date = models.DateTimeField('更新日期',auto_now_add=True)
    cls = models.CharField('类别',max_length=32,choices=PRODUCTS_2,default='概述')
    part = models.CharField('显示区域',max_length=32,choices=PART,default='part1')
    name = models.CharField('标题',max_length=256)
    purpore = models.CharField('小标题',max_length=256)
    content = models.TextField('更新内容')
    img = models.ImageField('资源图片',upload_to='product')
    
    objects = ProductResourceManager()
    
    def __unicode__(self):
        return self.name

class ProductSupplyManager(BaseModelManager):
    pass

class ProductSupply(models.Model):
    class Meta:
        verbose_name_plural = u'供应链管理系统'
        ordering = ['cls','name','-date']
        
    date = models.DateTimeField('更新日期',auto_now_add=True)
    cls = models.CharField('类别',max_length=32,choices=PRODUCTS_2,default='概述')
    part = models.CharField('显示区域',max_length=32,choices=PART,default='part1')
    name = models.CharField('标题',max_length=256)
    purpore = models.CharField('小标题',max_length=256)
    content = models.TextField('更新内容')
    img = models.ImageField('资源图片',upload_to='product')
    
    objects = ProductSupplyManager()
    
    def __unicode__(self):
        return self.name
    
class ProductHumanManager(BaseModelManager):
    pass

class ProductHuman(models.Model):
    class Meta:
        verbose_name_plural = u'供应链管理系统'
        ordering = ['cls','name','-date']
        
    date = models.DateTimeField('更新日期',auto_now_add=True)
    cls = models.CharField('类别',max_length=32,choices=PRODUCTS_2,default='概述')
    part = models.CharField('显示区域',max_length=32,choices=PART,default='part1')
    name = models.CharField('标题',max_length=256)
    purpore = models.CharField('小标题',max_length=256)
    content = models.TextField('更新内容')
    img = models.ImageField('资源图片',upload_to='product')
    
    objects = ProductHumanManager()
    
    def __unicode__(self):
        return self.name
    
class ProductContentManager(BaseModelManager):
    pass

class ProductContent(models.Model):
    class Meta:
        verbose_name_plural = u'内容管理系统'
        ordering = ['cls','name','-date']
        
    date = models.DateTimeField('更新日期',auto_now_add=True)
    cls = models.CharField('类别',max_length=32,choices=PRODUCTS_2,default='概述')
    part = models.CharField('显示区域',max_length=32,choices=PART,default='part1')
    name = models.CharField('标题',max_length=256)
    purpore = models.CharField('小标题',max_length=256)
    content = models.TextField('更新内容')
    img = models.ImageField('资源图片',upload_to='product')
    
    objects = ProductContentManager()
    
    def __unicode__(self):
        return self.name

class ProductOnlineManager(BaseModelManager):
    pass

class ProductOnline(models.Model):
    class Meta:
        verbose_name_plural = u'网上报销与费用管控系统'
        ordering = ['cls','name','-date']
        
    date = models.DateTimeField('更新日期',auto_now_add=True)
    cls = models.CharField('类别',max_length=32,choices=PRODUCTS_2,default='概述')
    part = models.CharField('显示区域',max_length=32,choices=PART,default='part1')
    name = models.CharField('标题',max_length=256)
    purpore = models.CharField('小标题',max_length=256)
    content = models.TextField('更新内容')
    img = models.ImageField('资源图片',upload_to='product')
    
    objects = ProductOnlineManager()
    
    def __unicode__(self):
        return self.name

class ProductDigitalManager(BaseModelManager):
    pass

class ProductDigital(models.Model):
    class Meta:
        verbose_name_plural = u'企业数字证书系统'
        ordering = ['cls','name','-date']
        
    date = models.DateTimeField('更新日期',auto_now_add=True)
    cls = models.CharField('类别',max_length=32,choices=PRODUCTS_3,default='概述')
    part = models.CharField('显示区域',max_length=32,choices=PART,default='part1')
    name = models.CharField('标题',max_length=256)
    purpore = models.CharField('小标题',max_length=256)
    content = models.TextField('更新内容')
    img = models.ImageField('资源图片',upload_to='product')
    
    objects = ProductDigitalManager()
    
    def __unicode__(self):
        return self.name

class ProductCustomerManager(BaseModelManager):
    pass

class ProductCustomer(models.Model):
    class Meta:
        verbose_name_plural = u'客户关系管理系统'
        ordering = ['cls','name','-date']
        
    date = models.DateTimeField('更新日期',auto_now_add=True)
    cls = models.CharField('类别',max_length=32,choices=PRODUCTS_3,default='概述')
    part = models.CharField('显示区域',max_length=32,choices=PART,default='part1')
    name = models.CharField('标题',max_length=256)
    purpore = models.CharField('小标题',max_length=256)
    content = models.TextField('更新内容')
    img = models.ImageField('资源图片',upload_to='product')
    
    objects = ProductCustomerManager()
    
    def __unicode__(self):
        return self.name
        
class ProductCoordinationAdmin(admin.ModelAdmin):
    list_display = ('date','cls','name','content','img')
class ProductResourceAdmin(admin.ModelAdmin):
    list_display = ('date','cls','name','content','img')
class ProductSupplyAdmin(admin.ModelAdmin):
    list_display = ('date','cls','name','content','img')   
class ProductHumanAdmin(admin.ModelAdmin):
    list_display = ('date','cls','name','content','img')
class ProductContentAdmin(admin.ModelAdmin):
    list_display = ('date','cls','name','content','img')
class ProductOnlineAdmin(admin.ModelAdmin):
    list_display = ('date','cls','name','content','img')
class ProductDigitalAdmin(admin.ModelAdmin):
    list_display = ('date','cls','name','content','img')   
class ProductCustomerAdmin(admin.ModelAdmin):
    list_display = ('date','cls','name','content','img')
    
admin.site.register(ProductCoordination, ProductCoordinationAdmin)
admin.site.register(ProductResource, ProductResourceAdmin)
admin.site.register(ProductSupply, ProductSupplyAdmin)
admin.site.register(ProductHuman, ProductHumanAdmin)
admin.site.register(ProductContent, ProductContentAdmin)
admin.site.register(ProductOnline, ProductOnlineAdmin)
admin.site.register(ProductDigital, ProductDigitalAdmin)
admin.site.register(ProductCustomer, ProductCustomerAdmin)