from django.shortcuts import render
from knowledge.models import Concept, Link, Relation
from django.http import JsonResponse
from datetime import datetime

# Create your views here.


def fields(request):
    return render(request, 'personal/create/fields.html', locals())


def concepts(request):
    all_concepts = Concept.objects.all()
    if request.method == 'POST':
        try:
            if request.POST['action'] == 'newConcept':
                ob = Concept.objects.create(_title=request.POST["title"])
                ob.create_time = datetime.now()
                ob.owner = request.user
                ob.save()
                print(request.POST["title"])
                return JsonResponse({'id': ob.id, 'title': ob.title, 'owner': str(ob.owner)})
        except EnvironmentError:
            pass
    return render(request, 'personal/create/concepts.html', locals())













