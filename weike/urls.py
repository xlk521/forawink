#coding=utf8
from django.conf.urls import patterns, include, url
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'home.views.home'),
    url(r'^product/', include('product.urls')),
    url(r'^solutions/', include('solutions.urls')),
    url(r'^service/', include('service.urls')),
    url(r'^case/', include('case.urls')),
    url(r'^about/', include('about.urls')),
)