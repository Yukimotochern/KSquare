from django.shortcuts import render

# Create your views here.


def fields(request):
    return render(request, 'personal/create/fields.html', locals())


def concepts(request):
    return render(request, 'personal/create/concepts.html', locals())













