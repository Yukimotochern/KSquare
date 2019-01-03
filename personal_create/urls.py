from django.contrib import admin
from django.urls import path, re_path
from . import views
from django.conf.urls import url, include

urlpatterns = [
    re_path('fields/(?P<tab>[0-1])?', views.fields, name="fields"),
    re_path('concepts/(?P<tab>[0-1])?', views.concepts, name="concepts"),
    re_path('templates/(?P<tab>[0-1])?', views.templates, name="templates"),

]