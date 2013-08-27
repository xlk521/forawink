#coding=utf8
from django.http import Http404
from django.shortcuts import render_to_response
from .models import *

'''
Development:应用软件开发
Support:信息技术支持
UIVI:UI/VI设计
'''
def get_data(request,model):
    service = model.objects.all()
    print 12345
    print service
    head = []
    content = []
    if service:
        i = 1
        for c in service:
            s = {}
            s['class'] = c.cls
            s['name'] = c.name
            s['content'] = c.content
            s['img'] = c.img
            s['num'] = i
            if c.cls == 'head':
                head.append(s)
            else:
                content.append(s)
            i = i+1
    result = {'head':head,'content':content}
    return result
def Development(request):
    return render_to_response('service/Development.html',get_data(request,ServiceDevelopment))

def Support(request):
    return render_to_response('service/Support.html',get_data(request,ServiceSupport))

def UIVI(request):
    return render_to_response('service/UIVI.html',get_data(request,ServiceUI))