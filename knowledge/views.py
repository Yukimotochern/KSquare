from django.shortcuts import render,redirect
# Create your views here.


def concept(request):
    return render(request, 'concept.html', locals())

