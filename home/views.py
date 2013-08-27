#coding=utf8
from django.http import Http404
from django.shortcuts import render_to_response
from .models import *

def home(request):
    home = HomeImg.objects.all()
    using = HomeUsingImg.objects.all()
    technology = HomeTechnologyImg.objects.all()
    ui = HomeUIImg.objects.all()
    case = HomeCaseImg.objects.all()
    homes = []
    usings = []
    technologys = []
    uis = []
    cases = []
    i = 1
    for c in home:
        s = {}
        s['img'] = c.img
        homes.append(s)
    for c in using:
        s = {}
        s['img'] = c.img
        usings.append(s)
    for c in technology:
        s = {}
        s['img'] = c.img
        technologys.append(s)
    for c in ui:
        s = {}
        s['img'] = c.img
        uis.append(s)
    for c in case:
        s = {}
        s['img'] = c.img
        s['num'] = i
        i=i+1
        cases.append(s)
    return render_to_response('home/home.html',{'homes':homes,'usings':usings,'technologys':technologys,'uis':uis,'cases':cases})