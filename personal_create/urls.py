from django.contrib import admin
from django.urls import path
from . import views
from django.conf.urls import url, include

urlpatterns = [
    path('fields/', views.fields, name="fields"),

]