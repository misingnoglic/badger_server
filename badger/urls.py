__author__ = 'arya'
from django.conf.urls import patterns, url

from badger import views
urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    #url(r'scantron/(?P<name>\w+)',views.scantron,name='scantron'),
    url(r'locations/(?P<id>\d+)/$',views.single_location,name="single_location"),
    url(r'locations/$',views.locations,name="locations"),
    url(r'badges/(?P<id>\d+)/$',views.single_badge,name="single_badge"),
    url(r'badges/$',views.badges,name="badges"),
    url(r'categories/(?P<id>\d+)/$',views.single_category,name="single_category"),
    url(r'categories/$',views.categories,name="categories"),
)
