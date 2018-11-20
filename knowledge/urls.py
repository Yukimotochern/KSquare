from django.contrib import admin
from django.urls import path
from . import views
from django.conf.urls import url, include

urlpatterns = [
    path('', views.concept_view, name="concept_manage"),
    path('concept/create', views.create_concept, name="create_concept"),
    path('concept/edit', views.edit_concept, name="edit_concept"),
    path('concept/edit/save', views.edit_concept_save, name="edit_concept_save"),
    path('concept/delete', views.delete_concept, name="delete_concept"),

    # path('relation/create',name=""),
    # path('relation/edit',name=""),
    # path('relation/delete',name=""),
    #
    # path('relation/entry/create', name=""),
    # path('relation/entry/edit',name=""),
    # path('relation/entry/delete',name=""),
]