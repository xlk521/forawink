#coding=utf8
from django.http import Http404
from django.shortcuts import render_to_response
from .models import About

def about(request):
	about = About.objects.filter(cls='公司简介')
	#about = About.objects.get_or_none(cls='公司简介')
	a = []
	print about
	if about:
		print about
		for b in about:
			abouts = {}
			abouts['purport'] = b.purport
			abouts['content'] = b.content
			abouts['img'] = b.img
			a.append(abouts)
	return render_to_response('about/about.html',{'abouts':a})