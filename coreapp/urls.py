from django.urls import re_path, include
from . import views

urlpatterns=[
    # amal
    re_path(r'^$', views.index, name='index'),
    re_path(r'^tldashboard$', views.tldashboard, name='tldashboard'),
    re_path(r'^tlprojects$', views.tlprojects, name='tlprojects'),
    re_path(r'^tlprojecttasks$', views.tlprojecttasks, name='tlprojecttasks'),
    re_path(r'^tlsplittask$', views.tlsplittask, name='tlsplittask'),
    re_path(r'^tlgivetask$', views.tlgivetask, name='tlgivetask'),
# abin
    re_path(r'^TLattendance$', views.TLattendance, name='TLattendance'),
    re_path(r'^TLreportissues$', views.TLreportissues, name='TLreportissues'),
    re_path(r'^TLreportedissue1$', views.TLreportedissue1, name='TLreportedissue1'),
    re_path(r'^TLreportedissue2$', views.TLreportedissue2, name='TLreportedissue2'),
    re_path(r'^TLreport1$', views.TLreport1, name='TLreport1'),
    re_path(r'^TLreportsuccess$', views.TLreportsuccess, name='TLreportsuccess'),
    # bibn
    re_path(r'^TLtasks$', views.TLtasks, name='TLtasks'),
    re_path(r'^TLleave$', views.TLleave, name='TLleave'),
    re_path(r'^TLleavereq$', views.TLleavereq, name='TLleavereq'),
    re_path(r'^TLreqedleave$', views.TLreqedleave, name='TLreqedleave'),
    re_path(r'^TLgivetask$', views.TLgivetask, name='TLgivetask'),
    re_path(r'^TLgavetask$', views.TLgavetask, name='TLgavetask'),
    re_path(r'^TLsuccess$', views.TLsuccess, name='TLsuccess'),
]