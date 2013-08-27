#coding=utf8
from django.conf.urls import patterns, include, url

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
urlpatterns = patterns('product.views',
    url(r'^Coordination/$','Coordination',name='Coordination'),
    url(r'^Resource/$','Resource',name='Resource'),
    url(r'^Supply/$','Supply',name='Supply'),
    url(r'^Human/$','Human',name='Human'),
    url(r'^Content/$','Content',name='Content'),
    url(r'^Online/$','Online',name='Online'),
    url(r'^Digital/$','Digital',name='Digital'),
    url(r'^Customer/$','Customer',name='Customer'),
)