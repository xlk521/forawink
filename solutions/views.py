#coding=utf8
from django.http import Http404, HttpResponse
from django.shortcuts import render_to_response
from .models import *
from utils import convertjson

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
def get_data(request,model):
    product = model.objects.filter(cls='概述')
    part1 = []
    part2 = []
    part3 = []
    if product:
        for c in product:
            s = {}
            s['name'] = c.name
            s['content'] = c.content
            s['img'] = c.img
            if c.part == 'part1':
                part1.append(s)
            elif c.part == 'part2':
                part2.append(s)
            elif c.part == 'part3':
                part3.append(s)
            else:break
    result = {'part1':part1,'part2':part2,'part3':part3}
    return result

def post_data(request,model,cls):
    product = model.objects.filter(cls=cls)
    part1 = []
    part2 = []
    part3 = []
    if product:
        for c in product:
            s = {}
            s['name'] = c.name
            s['content'] = c.content
            s['img_url'] = c.img.url
            if c.part == 'part1':
                part1.append(s)
            elif c.part == 'part2':
                part2.append(s)
            elif c.part == 'part3':
                part3.append(s)
            else:break
    result = {'part1':part1,'part2':part2,'part3':part3}
    return convertjson(result)

def get_or_post(request,html,model):
    if request.method == 'GET':
        return render_to_response(html,get_data(request,model))
    elif request.method == 'POST':
        cls = request.POST.get('cls', False)
        if cls:
            return HttpResponse(post_data(request,model,cls))
        else:
            return Http404()
        
def EG(request):
    return get_or_post(request,'solutions/EG.html',SolutionsEG)

def Management(request):
    return render_to_response('solutions/Management.html',get_data(request,SolutionsManagement))

def PublicHealth(request):
    return render_to_response('solutions/PublicHealth.html',get_data(request,SolutionsPublicHealth))

def DrugInvoicing(request):
    return render_to_response('solutions/DrugInvoicing.html',get_data(request,SolutionsDrugInvoicing))

def AudienceFeedback(request):
    return render_to_response('solutions/AudienceFeedback.html',get_data(request,SolutionsAudienceFeedback))

def PublicWelfare(request):
    return get_or_post(request,'solutions/PublicWelfare.html',SolutionsPublicWelfare)

def Assessment(request):
    return get_or_post(request,'solutions/Assessment.html',SolutionsAssessment)

def ForeignExchange(request):
    return render_to_response('solutions/ForeignExchange.html',get_data(request,SolutionsForeignExchange))

def LogisticsResource(request):
    return render_to_response('solutions/LogisticsResource.html',get_data(request,SolutionsLogisticsResource))

def NetworkPlatform(request):
    return render_to_response('solutions/NetworkPlatform.html',get_data(request,SolutionsNetworkPlatform))

def CloudStorage(request):
    return get_or_post(request,'solutions/CloudStorage.html',SolutionsCloudStorage)

def AquaticSales(request):
    return render_to_response('solutions/AquaticSales.html',get_data(request,SolutionsAquaticSales))

def FreightInformation(request):
    return render_to_response('solutions/FreightInformation.html',get_data(request,SolutionsFreightInformation))

def InsuranceAdjuster(request):
    return render_to_response('solutions/InsuranceAdjuster.html',get_data(request,SolutionsInsuranceAdjuster))

def SalesRebate(request):
    return render_to_response('solutions/SalesRebate.html',get_data(request,SolutionsSalesRebate))

def ElectronicCommerce(request):
    return render_to_response('solutions/ElectronicCommerce.html',get_data(request,SolutionsElectronicCommerce))

def MedicalServices(request):
    return get_or_post(request,'solutions/MedicalServices.html',SolutionsMedicalServices)

def ELearning(request):
    return render_to_response('solutions/ELearning.html',get_data(request,SolutionsELearning))

def InsuranceBusiness(request):
    return get_or_post(request,'solutions/InsuranceBusiness.html',SolutionsInsuranceBusiness)