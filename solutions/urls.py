#coding=utf8
from django.conf.urls import patterns, include, url

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
urlpatterns = patterns('solutions.views',
    url(r'^EG/$','EG',name='EG'),
    url(r'^Management/$','Management',name='Management'),
    url(r'^PublicHealth/$','PublicHealth',name='PublicHealth'),
    url(r'^DrugInvoicing/$','DrugInvoicing',name='DrugInvoicing'),
    url(r'^AudienceFeedback/$','AudienceFeedback',name='AudienceFeedback'),
    url(r'^PublicWelfare/$','PublicWelfare',name='PublicWelfare'),
    url(r'^Assessment/$','Assessment',name='Assessment'),
    url(r'^ForeignExchange/$','ForeignExchange',name='ForeignExchange'),
    url(r'^LogisticsResource/$','LogisticsResource',name='LogisticsResource'),
    url(r'^NetworkPlatform/$','NetworkPlatform',name='NetworkPlatform'),
    url(r'^CloudStorage/$','CloudStorage',name='CloudStorage'),
    url(r'^AquaticSales/$','AquaticSales',name='AquaticSales'),
    url(r'^FreightInformation/$','FreightInformation',name='FreightInformation'),
    url(r'^InsuranceAdjuster/$','InsuranceAdjuster',name='InsuranceAdjuster'),
    url(r'^SalesRebate/$','SalesRebate',name='SalesRebate'),
    url(r'^ElectronicCommerce/$','ElectronicCommerce',name='ElectronicCommerce'),
    url(r'^MedicalServices/$','MedicalServices',name='MedicalServices'),
    url(r'^ELearning/$','ELearning',name='ELearning'),
    url(r'^InsuranceBusiness/$','InsuranceBusiness',name='InsuranceBusiness'),
)