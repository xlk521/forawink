#coding=utf8
from django.http import Http404
from django.shortcuts import render_to_response
from .models import Case

def case(request):
    case = Case.objects.all()
    cases = []
    for c in case:
        s = {}
        s['name'] = c.name
        s['content'] = c.content
        s['img'] = c.img
        cases.append(s)
    return render_to_response('case/case.html',{'cases':cases})