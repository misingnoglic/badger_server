__author__ = 'arya'
from django.conf.urls import patterns, url

from badger import views
urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    )
