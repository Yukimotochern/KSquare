from . import views
from django.conf.urls import url, include

urlpatterns = [
    url(r'^register/$', views.register, name='register'),
]