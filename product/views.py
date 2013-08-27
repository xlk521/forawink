#coding=utf8
from django.http import HttpResponse, Http404
from django.shortcuts import render_to_response
from .models import *
from utils import convertjson

'''
Coordination
Resource
Supply
Human
Content
Online
Digital
Customer
'''
def get_data(request,model):
    product = model.objects.filter(cls='概述')
    print 12345
    print product
    part1 = []
    part2 = []
    part3 = []
    part4 = []
    if product:
        print '09876'
        for c in product:
            s = {}
            s['name'] = c.name
            s['content'] = c.content
            s['purpore'] = c.purpore
            s['img'] = c.img
            print c.part
            if c.part == 'part1':
                part1.append(s)
                print part1
            elif c.part == 'part2':
                part2.append(s)
            elif c.part == 'part3':
                part3.append(s)
            elif c.part == 'part4':
                part4.append(s)
            else:break
    result = {'part1':part1,'part2':part2,'part3':part3,'part4':part4}
    return result

def post_data(request,model,cls):
    product = model.objects.filter(cls=cls)
    part1 = []
    part2 = []
    part3 = []
    part4 = []
    if product:
        for c in product:
            s = {}
            s['name'] = c.name
            s['content'] = c.content
            s['purpore'] = c.purpore
            s['img_url'] = c.img.url
            if c.part == 'part1':
                part1.append(s)
            elif c.part == 'part2':
                part2.append(s)
            elif c.part == 'part3':
                part3.append(s)
            elif c.part == 'part4':
                part4.append(s)
            else:break
    result = {'part1':part1,'part2':part2,'part3':part3,'part4':part4}
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

def Coordination(request):
    return get_or_post(request,'product/Coordination.html',ProductCoordination)

def Resource(request):
    return get_or_post(request,'product/Resource.html',ProductResource)

def Supply(request):
    return get_or_post(request,'product/Supply.html',ProductSupply)

def Human(request):
    return get_or_post(request,'product/Human.html',ProductHuman)

def Content(request):
    return get_or_post(request,'product/Content.html',ProductContent)

def Online(request):
    return get_or_post(request,'product/Online.html',ProductOnline)

def Digital(request):
    return get_or_post(request,'product/Digital.html',ProductDigital)

def Customer(request):
    return get_or_post(request,'product/Customer.html',ProductCustomer)