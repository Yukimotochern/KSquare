from django.shortcuts import render
from knowledge.models import Concept, Link, Relation
from django.http import JsonResponse
from datetime import datetime
from django import utils
from django.utils import timezone

# Create your views here.


def fields(request):
    return render(request, 'personal/create/fields.html', locals())


def concepts(request):
    all_concepts = Concept.objects.all().order_by('id').reverse()
    if request.method == 'POST':
        try:
            if request.POST['action'] == 'newConcept':
                ob = Concept.objects.create(_title=request.POST["title"])
                ob.summary = request.POST['summary']
                ob.create_time = timezone.now()
                ob.owner = request.user
                ob.save()
                return JsonResponse({'id': ob.id, 'title': ob.title, 'owner': str(ob.owner)})
            elif request.POST['action'] == 'updateConcept':
                try:
                    ob = Concept.objects.get(id=request.POST['id'])
                    ob.title = request.POST['title']
                    ob.summary = request.POST['summary']
                    ob.modify_time = timezone.now()
                    ob.save()
                    return JsonResponse({'id': ob.id})
                except utils.datastructures.MultiValueDictKeyError:
                    pass
            elif request.POST['action'] == 'deleteConcept':
                try:
                    id_to_delete = int(request.POST['id'])
                    ob = Concept.objects.get(id=id_to_delete)
                    ob.delete()
                    return JsonResponse({'id': id_to_delete})
                except:
                    pass
        except EnvironmentError:
            pass
    return render(request, 'personal/create/concepts.html', locals())













