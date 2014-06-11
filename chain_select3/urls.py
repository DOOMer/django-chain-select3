# coding: utf8

from django.conf.urls import patterns, url


urlpatterns = patterns('chain_select3.views',
    url(r'^(?P<app_name>[\w\-]+)/'
        '(?P<model_name>[\w\-]+)/'
        '(?P<method_name>[\w\-]+)/'
        '(?P<pk>[\w\-]+)/$',
        'filterchain_all',
        name='filter_all'),
)
