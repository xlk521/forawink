#coding=utf8
from django.db import models
from django.contrib.auth.models import AbstractBaseUser , BaseUserManager
from django.contrib import admin
from utils.base import BaseModelManager

'''
电子政务  :  EG
企业档案管理  :  Management
公共卫生检测  :  PublicHealth
药品进销存  : DrugInvoicing
受众信息反馈  :  AudienceFeedback
公益捐赠  :  PublicWelfare
企业人才测评  : Assessment
外汇辅助交易  :ForeignExchange
物流资源网络平台  :  LogisticsResource
物联网网络平台  :  NetworkPlatform
云存储系统  :  CloudStorage
水产销售管理  :  AquaticSales
货运信息  :  FreightInformation
保险公估  :  InsuranceAdjuster
销售提成返利  :  SalesRebate
企业电子商务  :  ElectronicCommerce
医疗服务  :  MedicalServices
E-Learning培训  :  ELearning
保险经济业务  :  InsuranceBusiness
'''
'''
class:
                概述 :Summary
                功能 :Function
                架构 :Framework
                特点 :Characteristic
                技术 :Technology
                服务 : Service
'''
PRODUCTS_4= (
        ('概述', '概述'),
        ('特点', '特点'),
        ('技术', '技术'),
        ('服务', '服务'),
    )
PRODUCTS_2= (
        ('概述', '概述'),
        ('功能', '功能'),
    )
PART= (
        ('part1', 'part1:一组'),
        ('part2', 'part2:一组'),
        ('part3', 'part3:多组'),
    )

class SolutionsEGManager(BaseModelManager):
    pass

class SolutionsEG(models.Model):
    class Meta:
        verbose_name_plural = u'电子政务解决方案:概述、功能、架构'
        ordering = ['cls','name','date']
    
    PRODUCTS_3= (
        ('概述', '概述'),
        ('功能', '功能'),
        ('架构', '架构'),
    )
    date = models.DateTimeField('更新日期',auto_now_add=True)
    cls = models.CharField('类别',max_length=32,choices=PRODUCTS_3,default='概述')
    part = models.CharField('显示区域',max_length=32,choices=PART,default='part1')
    name = models.CharField('标题',max_length=256)
    content = models.TextField('更新内容')
    img = models.ImageField('资源图片',upload_to='solutions')
    
    objects = SolutionsEGManager()
    
    def __unicode__(self):
        return self.name

class SolutionsManagementManager(BaseModelManager):
    pass

class SolutionsManagement(models.Model):
    class Meta:
        verbose_name_plural = u'企业档案管理解决方案:概述'
        ordering = ['cls','name','date']
        
    date = models.DateTimeField('更新日期',auto_now_add=True)
    cls = models.CharField('类别',max_length=32,default='概述')
    part = models.CharField('显示区域',max_length=32,choices=PART,default='part1')
    name = models.CharField('标题',max_length=256)
    content = models.TextField('更新内容')
    img = models.ImageField('资源图片',upload_to='solutions')
    
    objects = SolutionsManagementManager()
    
    def __unicode__(self):
        return self.name
    
class SolutionsPublicHealthManager(BaseModelManager):
    pass

class SolutionsPublicHealth(models.Model):
    class Meta:
        verbose_name_plural = u'公共卫生监测解决方案:概述'
        ordering = ['cls','name','date']
        
    date = models.DateTimeField('更新日期',auto_now_add=True)
    cls = models.CharField('类别',max_length=32,default='概述')
    part = models.CharField('显示区域',max_length=32,choices=PART,default='part1')
    name = models.CharField('标题',max_length=256)
    content = models.TextField('更新内容')
    img = models.ImageField('资源图片',upload_to='solutions')
    
    objects = SolutionsPublicHealthManager()
    
    def __unicode__(self):
        return self.name
    
class SolutionsDrugInvoicingManager(BaseModelManager):
    pass

class SolutionsDrugInvoicing(models.Model):
    class Meta:
        verbose_name_plural = u'药品进销存管理决方案:概述'
        ordering = ['cls','name','date']
        
    date = models.DateTimeField('更新日期',auto_now_add=True)
    cls = models.CharField('类别',max_length=32,default='概述')
    part = models.CharField('显示区域',max_length=32,choices=PART,default='part1')
    name = models.CharField('标题',max_length=256)
    content = models.TextField('更新内容')
    img = models.ImageField('资源图片',upload_to='solutions')
    
    objects = SolutionsDrugInvoicingManager()
    
    def __unicode__(self):
        return self.name
    
class SolutionsAudienceFeedbackManager(BaseModelManager):
    pass

class SolutionsAudienceFeedback(models.Model):
    class Meta:
        verbose_name_plural = u'受众信息反馈系统:概述'
        ordering = ['cls','name','date']
        
    date = models.DateTimeField('更新日期',auto_now_add=True)
    cls = models.CharField('类别',max_length=32,default='概述')
    part = models.CharField('显示区域',max_length=32,choices=PART,default='part1')
    name = models.CharField('标题',max_length=256)
    content = models.TextField('更新内容')
    img = models.ImageField('资源图片',upload_to='solutions')
    
    objects = SolutionsAudienceFeedbackManager()
    
    def __unicode__(self):
        return self.name
    
class SolutionsPublicWelfareManager(BaseModelManager):
    pass

class SolutionsPublicWelfare(models.Model):
    class Meta:
        verbose_name_plural = u'公益捐赠解决方案:概述、特点、技术'
        ordering = ['cls','name','date']
        
    PRODUCTS_3= (
        ('概述', '概述'),
        ('特点', '特点'),
        ('技术', '技术'),
    )
    date = models.DateTimeField('更新日期',auto_now_add=True)
    cls = models.CharField('类别',max_length=32,choices=PRODUCTS_3,default='概述')
    part = models.CharField('显示区域',max_length=32,choices=PART,default='part1')
    name = models.CharField('标题',max_length=256)
    content = models.TextField('更新内容')
    img = models.ImageField('资源图片',upload_to='solutions')
    
    objects = SolutionsPublicWelfareManager()
    
    def __unicode__(self):
        return self.name
    
class SolutionsAssessmentManager(BaseModelManager):
    pass

class SolutionsAssessment(models.Model):
    class Meta:
        verbose_name_plural = u'企业人才测评解决方案:概述、功能、技术'
        ordering = ['cls','name','date']
        
    PRODUCTS_3= (
        ('概述', '概述'),
        ('功能', '功能'),
        ('技术', '技术'),
    )
    date = models.DateTimeField('更新日期',auto_now_add=True)
    cls = models.CharField('类别',max_length=32,choices=PRODUCTS_3,default='概述')
    part = models.CharField('显示区域',max_length=32,choices=PART,default='part1')
    name = models.CharField('标题',max_length=256)
    content = models.TextField('更新内容')
    img = models.ImageField('资源图片',upload_to='solutions')
    
    objects = SolutionsAssessmentManager()
    
    def __unicode__(self):
        return self.name
    
class SolutionsForeignExchangeManager(BaseModelManager):
    pass

class SolutionsForeignExchange(models.Model):
    class Meta:
        verbose_name_plural = u'外汇辅助交易解决方案:概述'
        ordering = ['cls','name','date']
        
    date = models.DateTimeField('更新日期',auto_now_add=True)
    cls = models.CharField('类别',max_length=32,default='概述')
    part = models.CharField('显示区域',max_length=32,choices=PART,default='part1')
    name = models.CharField('标题',max_length=256)
    content = models.TextField('更新内容')
    img = models.ImageField('资源图片',upload_to='solutions')
    
    objects = SolutionsForeignExchangeManager()
    
    def __unicode__(self):
        return self.name
    
class SolutionsLogisticsResourceManager(BaseModelManager):
    pass

class SolutionsLogisticsResource(models.Model):
    class Meta:
        verbose_name_plural = u'物流资源网络平台解决方案:概述'
        ordering = ['cls','name','date']
        
    date = models.DateTimeField('更新日期',auto_now_add=True)
    cls = models.CharField('类别',max_length=32,default='概述')
    part = models.CharField('显示区域',max_length=32,choices=PART,default='part1')
    name = models.CharField('标题',max_length=256)
    content = models.TextField('更新内容')
    img = models.ImageField('资源图片',upload_to='solutions')
    
    objects = SolutionsLogisticsResourceManager()
    
    def __unicode__(self):
        return self.name
    
class SolutionsNetworkPlatformManager(BaseModelManager):
    pass

class SolutionsNetworkPlatform(models.Model):
    class Meta:
        verbose_name_plural = u'物联网网络平台解决方案:概述'
        ordering = ['cls','name','date']
        
    date = models.DateTimeField('更新日期',auto_now_add=True)
    cls = models.CharField('类别',max_length=32,default='概述')
    part = models.CharField('显示区域',max_length=32,choices=PART,default='part1')
    name = models.CharField('标题',max_length=256)
    content = models.TextField('更新内容')
    img = models.ImageField('资源图片',upload_to='solutions')
    
    objects = SolutionsNetworkPlatformManager()
    
    def __unicode__(self):
        return self.name
    
class SolutionsCloudStorageManager(BaseModelManager):
    pass

class SolutionsCloudStorage(models.Model):
    class Meta:
        verbose_name_plural = u'云存储系统解决方案:概述、特点、服务、技术'
        ordering = ['cls','name','date']
        
    date = models.DateTimeField('更新日期',auto_now_add=True)
    cls = models.CharField('类别',max_length=32,choices=PRODUCTS_4,default='概述')
    part = models.CharField('显示区域',max_length=32,choices=PART,default='part1')
    name = models.CharField('标题',max_length=256)
    content = models.TextField('更新内容')
    img = models.ImageField('资源图片',upload_to='solutions')
    
    objects = SolutionsCloudStorageManager()
    
    def __unicode__(self):
        return self.name
    
class SolutionsAquaticSalesManager(BaseModelManager):
    pass

class SolutionsAquaticSales(models.Model):
    class Meta:
        verbose_name_plural = u'水产销售管理解决方案:概述'
        ordering = ['cls','name','date']
        
    date = models.DateTimeField('更新日期',auto_now_add=True)
    cls = models.CharField('类别',max_length=32,default='概述')
    part = models.CharField('显示区域',max_length=32,choices=PART,default='part1')
    name = models.CharField('标题',max_length=256)
    content = models.TextField('更新内容')
    img = models.ImageField('资源图片',upload_to='solutions')
    
    objects = SolutionsAquaticSalesManager()
    
    def __unicode__(self):
        return self.name
    
class SolutionsFreightInformationManager(BaseModelManager):
    pass

class SolutionsFreightInformation(models.Model):
    class Meta:
        verbose_name_plural = u'货运信息平台解决方案:概述'
        ordering = ['cls','name','date']
        
    date = models.DateTimeField('更新日期',auto_now_add=True)
    cls = models.CharField('类别',max_length=32,default='概述')
    part = models.CharField('显示区域',max_length=32,choices=PART,default='part1')
    name = models.CharField('标题',max_length=256)
    content = models.TextField('更新内容')
    img = models.ImageField('资源图片',upload_to='solutions')
    
    objects = SolutionsFreightInformationManager()
    
    def __unicode__(self):
        return self.name
    
class SolutionsInsuranceAdjusterManager(BaseModelManager):
    pass

class SolutionsInsuranceAdjuster(models.Model):
    class Meta:
        verbose_name_plural = u'保险公估业务平台解决方案:概述、功能'
        ordering = ['cls','name','date']
        
    date = models.DateTimeField('更新日期',auto_now_add=True)
    cls = models.CharField('类别',max_length=32,choices=PRODUCTS_2,default='概述')
    part = models.CharField('显示区域',max_length=32,choices=PART,default='part1')
    name = models.CharField('标题',max_length=256)
    content = models.TextField('更新内容')
    img = models.ImageField('资源图片',upload_to='solutions')
    
    objects = SolutionsInsuranceAdjusterManager()
    
    def __unicode__(self):
        return self.name
    
class SolutionsSalesRebateManager(BaseModelManager):
    pass

class SolutionsSalesRebate(models.Model):
    class Meta:
        verbose_name_plural = u'销售提成返利系统:概述'
        ordering = ['cls','name','date']
        
    date = models.DateTimeField('更新日期',auto_now_add=True)
    cls = models.CharField('类别',max_length=32,default='概述')
    part = models.CharField('显示区域',max_length=32,choices=PART,default='part1')
    name = models.CharField('标题',max_length=256)
    content = models.TextField('更新内容')
    img = models.ImageField('资源图片',upload_to='solutions')
    
    objects = SolutionsSalesRebateManager()
    
    def __unicode__(self):
        return self.name
    
class SolutionsElectronicCommerceManager(BaseModelManager):
    pass

class SolutionsElectronicCommerce(models.Model):
    class Meta:
        verbose_name_plural = u'企业电子商务解决方案:概述'
        ordering = ['cls','name','date']
        
    date = models.DateTimeField('更新日期',auto_now_add=True)
    cls = models.CharField('类别',max_length=32,default='概述')
    part = models.CharField('显示区域',max_length=32,choices=PART,default='part1')
    name = models.CharField('标题',max_length=256)
    content = models.TextField('更新内容')
    img = models.ImageField('资源图片',upload_to='solutions')
    
    objects = SolutionsElectronicCommerceManager()
    
    def __unicode__(self):
        return self.name
    
class SolutionsMedicalServicesManager(BaseModelManager):
    pass

class SolutionsMedicalServices(models.Model):
    class Meta:
        verbose_name_plural = u'医疗服务解决方案:概述、功能'
        ordering = ['cls','name','date']
        
    date = models.DateTimeField('更新日期',auto_now_add=True)
    cls = models.CharField('类别',max_length=32,choices=PRODUCTS_2,default='概述')
    part = models.CharField('显示区域',max_length=32,choices=PART,default='part1')
    name = models.CharField('标题',max_length=256)
    content = models.TextField('更新内容')
    img = models.ImageField('资源图片',upload_to='solutions')
    
    objects = SolutionsMedicalServicesManager()
    
    def __unicode__(self):
        return self.name
    
class SolutionsELearningManager(BaseModelManager):
    pass

class SolutionsELearning(models.Model):
    class Meta:
        verbose_name_plural = u'E-Learning培训解决方案:概述'
        ordering = ['cls','name','date']
        
    date = models.DateTimeField('更新日期',auto_now_add=True)
    cls = models.CharField('类别',max_length=32,default='概述')
    part = models.CharField('显示区域',max_length=32,choices=PART,default='part1')
    name = models.CharField('标题',max_length=256)
    content = models.TextField('更新内容')
    img = models.ImageField('资源图片',upload_to='solutions')
    
    objects = SolutionsELearningManager()
    
    def __unicode__(self):
        return self.name
    
class SolutionsInsuranceBusinessManager(BaseModelManager):
    pass

class SolutionsInsuranceBusiness(models.Model):
    class Meta:
        verbose_name_plural = u'保险经纪业务平台解决方案:概述、功能'
        ordering = ['cls','name','date']
        
    date = models.DateTimeField('更新日期',auto_now_add=True)
    cls = models.CharField('类别',max_length=32,choices=PRODUCTS_2,default='概述')
    part = models.CharField('显示区域',max_length=32,choices=PART,default='part1')
    name = models.CharField('标题',max_length=256)
    content = models.TextField('更新内容')
    img = models.ImageField('资源图片',upload_to='solutions')
    
    objects = SolutionsInsuranceBusinessManager()
    
    def __unicode__(self):
        return self.name
        
class SolutionsEGAdmin(admin.ModelAdmin):
    list_display = ('date','cls','name','content','img')
class SolutionsManagementAdmin(admin.ModelAdmin):
    list_display = ('date','cls','name','content','img')
class SolutionsPublicHealthAdmin(admin.ModelAdmin):
    list_display = ('date','cls','name','content','img')
class SolutionsDrugInvoicingAdmin(admin.ModelAdmin):
    list_display = ('date','cls','name','content','img')
class SolutionsAudienceFeedbackAdmin(admin.ModelAdmin):
    list_display = ('date','cls','name','content','img')
class SolutionsPublicWelfareAdmin(admin.ModelAdmin):
    list_display = ('date','cls','name','content','img')
class SolutionsAssessmentAdmin(admin.ModelAdmin):
    list_display = ('date','cls','name','content','img')
class SolutionsForeignExchangeAdmin(admin.ModelAdmin):
    list_display = ('date','cls','name','content','img')
class SolutionsLogisticsResourceAdmin(admin.ModelAdmin):
    list_display = ('date','cls','name','content','img')
class SolutionsNetworkPlatformAdmin(admin.ModelAdmin):
    list_display = ('date','cls','name','content','img')
class SolutionsCloudStorageAdmin(admin.ModelAdmin):
    list_display = ('date','cls','name','content','img')
class SolutionsAquaticSalesAdmin(admin.ModelAdmin):
    list_display = ('date','cls','name','content','img')
class SolutionsFreightInformationAdmin(admin.ModelAdmin):
    list_display = ('date','cls','name','content','img')
class SolutionsInsuranceAdjusterAdmin(admin.ModelAdmin):
    list_display = ('date','cls','name','content','img')
class SolutionsSalesRebateAdmin(admin.ModelAdmin):
    list_display = ('date','cls','name','content','img')
class SolutionsElectronicCommerceAdmin(admin.ModelAdmin):
    list_display = ('date','cls','name','content','img')
class SolutionsMedicalServicesAdmin(admin.ModelAdmin):
    list_display = ('date','cls','name','content','img')
class SolutionsELearningAdmin(admin.ModelAdmin):
    list_display = ('date','cls','name','content','img')
class SolutionsInsuranceBusinessAdmin(admin.ModelAdmin):
    list_display = ('date','cls','name','content','img')
    
admin.site.register(SolutionsEG, SolutionsEGAdmin)
admin.site.register(SolutionsManagement, SolutionsManagementAdmin)
admin.site.register(SolutionsPublicHealth, SolutionsPublicHealthAdmin)
admin.site.register(SolutionsDrugInvoicing, SolutionsDrugInvoicingAdmin)
admin.site.register(SolutionsAudienceFeedback, SolutionsAudienceFeedbackAdmin)
admin.site.register(SolutionsPublicWelfare, SolutionsPublicWelfareAdmin)
admin.site.register(SolutionsAssessment, SolutionsAssessmentAdmin)
admin.site.register(SolutionsForeignExchange, SolutionsForeignExchangeAdmin)
admin.site.register(SolutionsLogisticsResource, SolutionsLogisticsResourceAdmin)
admin.site.register(SolutionsNetworkPlatform, SolutionsNetworkPlatformAdmin)
admin.site.register(SolutionsCloudStorage, SolutionsCloudStorageAdmin)
admin.site.register(SolutionsAquaticSales, SolutionsAquaticSalesAdmin)
admin.site.register(SolutionsFreightInformation, SolutionsFreightInformationAdmin)
admin.site.register(SolutionsInsuranceAdjuster, SolutionsInsuranceAdjusterAdmin)
admin.site.register(SolutionsSalesRebate, SolutionsSalesRebateAdmin)
admin.site.register(SolutionsElectronicCommerce, SolutionsElectronicCommerceAdmin)
admin.site.register(SolutionsMedicalServices, SolutionsMedicalServicesAdmin)
admin.site.register(SolutionsELearning, SolutionsELearningAdmin)
admin.site.register(SolutionsInsuranceBusiness, SolutionsInsuranceBusinessAdmin)