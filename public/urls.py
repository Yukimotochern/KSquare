from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from . import views
from display.views import tag_view, ArticleListView, search_index
from django.views.generic.base import TemplateView

urlpatterns = [
    path('TagView/<tag_id>/', tag_view,name='TagView'),
    path('result/', ArticleListView.as_view(), name='result'),
    path('search/', search_index, name='search'),
    path('', TemplateView.as_view(template_name='outter/index.html'), name='home'),
]
