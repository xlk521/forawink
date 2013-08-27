#!/usr/bin/python 
# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import AbstractBaseUser , BaseUserManager
from utils.base import BaseModelManager
from django.contrib import admin
from django.db.models.signals import post_save, pre_save
from django.forms import ModelForm
import logging

class ProvinceManager(BaseModelManager):
    #creat a class of manager,but it has nothing.
    pass

class Province(models.Model):
    class Meta:
        verbose_name_plural = u'省级名称'
        ordering = ['ordering_letter']
        
    ordering_letter = models.CharField(max_length=2)
    name = models.CharField(primary_key=True,max_length=128)
    
    objects = ProvinceManager()
    
    def __unicode__(self):
        return self.name
    
class CityManager(BaseModelManager):
    pass

class City(models.Model):
    class Meta:
        verbose_name_plural = u"城市"
        unique_together = ('name',"province")
        ordering = ["ordering_letter"]
        
    ordering_letter = models.CharField(max_length=2)
    name = models.CharField(max_length=128)
    province = models.ForeignKey(Province)
    
    objects = CityManager()
    
    def __unicode__(self):
        return self.name
    
class CityInLine(admin.TabularInline):
    model = City
    def formfield_for_foreignkey(self,db_field,request=None,**kwargs):
        field = super(CityInLine, self).formfield_for_foreignkey(db_field, request, **kwargs)
        if db_field.name == 'inside_root':
            if request._obj_ is not None:
                field.queryset = field.queryset.filter(building__exact=request._obj_)
            else:
                field.queryset = field.queryset.none()

class UserManager(BaseUserManager):
    def create_user(self, identifier, password=None):
        if not identifier:
            raise ValueError('user:需要窜入一个用于识别的字符串！')
        
        user = self.model(
                          identifier = identifier,
                          )
        user.set_password(password)
        user.save(using = self._db)
        return user
    
    def create_superuser(self, identifier, password):
        user = self.create_user(identifier=identifier,password=password)
        user.is_admin = True
        user.save(using = self._db)
        return user
    
class User(AbstractBaseUser):
    class Meta:
        verbose_name_plural = u"用户信息"
        
    GENDER_CHOICES = ((True,'M'),(False,"W"))
        
    identifier = models.CharField(max_length=128, unique=True, db_index=True)
    nickname = models.CharField(max_length=256)
    gender = models.BooleanField(choices=GENDER_CHOICES)
    head = models.ImageField(upload_to="head")
    introduction = models.TextField(blank=True)
    city = models.ForeignKey(City,blank=True,null=True)
    province = models.ForeignKey(Province,blank=True,null=True)
    mobile = models.CharField(max_length=13,null=True)
    mobile_varified = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    
    objects = UserManager()
    
    def get_full_name(self):
        # The user is identified by their email address
        return self.nickname or self.identifier
    
    def get_short_name(self):
        # The user is identified by their email address
        return self.nickname or self.identifier

    def __unicode__(self):
        return self.nickname or self.identifier

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin
    
    
class WeiboUserManager(BaseModelManager):
    pass

class WeiboUser(models.Model):
    class Meta:
        verbose_name_plural = '微博账户信息'

    user = models.OneToOneField(User, primary_key=True)
    access_token = models.CharField('通过验证否', max_length=128, blank=True)
    expires_in = models.IntegerField("过期时间", blank=True)
    uid = models.CharField(max_length=128)
    name = models.CharField("友好显示名称", max_length=128)
    screen_name = models.CharField("用户昵称", max_length=128)
    province = models.CharField("省份", max_length=128)
    city = models.CharField("市", max_length=128)
    location = models.CharField("用户所在地", max_length=128, blank=True)
    description = models.TextField("个人描述", blank=True)
    url = models.CharField("用户博客地址", max_length=256, blank=True)
    profile_image_url = models.URLField()
    domain = models.CharField(max_length=128, blank=True)
    gender = models.CharField(max_length=2)
    followers_count = models.IntegerField()
    friends_count = models.IntegerField()
    statuses_count = models.IntegerField()
    favourites_count = models.IntegerField()
    created_at = models.DateTimeField()
    following = models.BooleanField()
    allow_all_act_msg = models.BooleanField()
    geo_enabled = models.BooleanField()
    verified = models.BooleanField(blank=True)
    allow_all_comment = models.BooleanField("是否允许所有人对我的微博进行评论")
    avatar_large = models.URLField("用户大头像地址")
    verified_reason = models.CharField("认证原因", max_length=128, blank=True)
    follow_me = models.BooleanField("该用户是否关注当前登录用户")
    online_status = models.IntegerField("用户的在线状态0:不在线1:在线")
    bi_followers_count = models.IntegerField("用户的互粉数")

    objects = WeiboUserManager()
    
    def __unicode__(self):
        return self.access_token
    
class WeiboUserForm(ModelForm):
    class Meta:
        model = WeiboUser
        exclude = ('user',)
        
class CityAdmin(admin.ModelAdmin):
    list_display = ('ordering_letter', 'name',)
    
class UserAdmin(admin.ModelAdmin):
    list_display = ('identifier','nickname','gender')

class WeiboUserAdmin(admin.ModelAdmin):
    list_display = ('uid','name')
'''
class WechatUserAdmin(admin.ModelAdmin):
    list_display = ('access_token',)
'''
class ProvinceAdmin(admin.ModelAdmin):
    inlines = (CityInLine,)
    list_display = ('name',)

    def get_form(self, request, obj=None, **kwargs):
        request._obj_ = obj
        return super(ProvinceAdmin, self).get_form(request, obj, **kwargs)

admin.site.register(Province, ProvinceAdmin)
admin.site.register(City, CityAdmin)
admin.site.register(User, UserAdmin)
admin.site.register(WeiboUser, WeiboUserAdmin)