from django.shortcuts import render,redirect
from django.contrib.auth import authenticate
from django.contrib import auth
from django.http import HttpResponse
from django.contrib.auth.models import User


def home(request):

    return render(request, 'homepage.html', locals())

