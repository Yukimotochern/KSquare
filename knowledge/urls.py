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

    path('relation/(?P<tab>[0-1])?', views.relation_view, name="relation_manage"),
    path('relation/create/(?P<tab>[0-1])?$', views.create_relation, name="create_relation"),
    path('relation/edit/(?P<tab>[0-1])?$', views.edit_relation, name="edit_relation"),
    path('relation/edit/save/(?P<tab>[0-1])?$', views.edit_relation_save, name="edit_relation_save"),
    path('relation/delete/(?P<tab>[0-1])?$', views.delete_relation, name="delete_relation"),

    path('relation/link/create/(?P<tab>[0-1])', views.create_link, name="create_link"),
    path('relation/link/edit/(?P<tab>[0-1])', views.edit_link, name="edit_link"),
    path('relation/link/save/(?P<tab>[0-1])', views.edit_link_save, name="edit_link_save"),
    path('relation/link/delete/(?P<tab>[0-1])', views.delete_link, name="delete_link"),

    path('relation/link/get_to_title', views.find_to_name, name="find_to_name"),

    url(r'square-tree/(?P<main_view_id>[0-9]+)/view/(?P<tab>[0-1])?', views.tree, name="learn"),
    path('total_explore//(?P<tab>[0-1])?', views.all_concepts, name='all_concept'),


]


