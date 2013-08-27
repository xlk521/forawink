#coding=utf8
from django.http import Http404
from django.shortcuts import render_to_response

def home(request):
    return render_to_response('home.html')

def product(request):
    return render_to_response('product.html')

def solutions(request):
    return render_to_response('solutions.html')

def service(request):
    return render_to_response('service.html')

def case(request):
    return render_to_response('case.html')

def about(request):
    return render_to_response('about.html')