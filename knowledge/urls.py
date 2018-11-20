from django.contrib import admin
from django.urls import path
from . import views
from django.conf.urls import url, include

urlpatterns = [
    path('', views.concept, name="createconcept"),
    # path('concept/create', ),
    # path('concept/edit', ),
    # path('concept/delete',),

    # path('relation/create',),
    # path('relation/edit',),
    # path('relation/delete',),
    #
    # path('relation/entry/create', ),
    # path('relation/entry/edit',),
    # path('relation/entry/delete',),
]