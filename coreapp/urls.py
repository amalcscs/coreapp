from django.urls import re_path, include
from . import views

urlpatterns=[
    re_path(r'^$', views.index, name='index'),
    re_path(r'^tldashboard$', views.tldashboard, name='tldashboard'),
    re_path(r'^tlprojects$', views.tlprojects, name='tlprojects'),
    re_path(r'^tlprojecttasks$', views.tlprojecttasks, name='tlprojecttasks'),
    re_path(r'^tlsplittask$', views.tlsplittask, name='tlsplittask'),
    re_path(r'^tlgivetask$', views.tlgivetask, name='tlgivetask'),
]