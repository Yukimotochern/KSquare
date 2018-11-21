from django.contrib import admin
from django.urls import path
from . import views
from django.conf.urls import url, include

urlpatterns = [
    path('concept/', views.concept_view, name="concept_manage"),
    path('concept/create', views.create_concept, name="create_concept"),
    path('concept/edit', views.edit_concept, name="edit_concept"),
    path('concept/edit/save', views.edit_concept_save, name="edit_concept_save"),
    path('concept/delete', views.delete_concept, name="delete_concept"),

    path('relation/', views.relation_view, name="relation_manage"),
    path('relation/create', views.create_relation, name="create_relation"),
    path('relation/edit', views.edit_relation, name="edit_relation"),
    path('relation/edit/save', views.edit_relation_save, name="edit_relation_save"),
    path('relation/delete', views.delete_relation, name="delete_relation"),
    #
    # path('relation/entry/create', name=""),
    # path('relation/entry/edit',name=""),
    # path('relation/entry/delete',name=""),
]