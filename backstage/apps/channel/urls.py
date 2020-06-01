# -*- coding: utf-8 -*-

from django.conf.urls import url
from channel import views

urlpatterns = [
    url('',views.test,name='test'),
    # url('importexcel/$',views.ImportKDOrderNo.as_view(),name='importkdorderno'),
]