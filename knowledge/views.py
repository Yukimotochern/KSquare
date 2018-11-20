from django.shortcuts import render,redirect
from knowledge.models import Concept, Relation, ToRelationEntry, ForthRelationEntry
# Create your views here.


def concept_view(request):
    concept = Concept.objects.all().order_by('id')
    return render(request, 'concept.html', locals())


def create_concept(request):
    dd = Concept.objects.create(title=request.POST["newtitle"], content=request.POST["newcontent"])
    concept = Concept.objects.all().order_by('id')
    return render(request, 'concept.html', locals())


def edit_concept(request):
    edit_id = request.POST["edit_id"]
    concept = Concept.objects.all().order_by('id')
    return render(request, 'concept.html', locals())


def edit_concept_save(request):
    try:
        to_edit = Concept.objects.get(id=int(request.POST["toedit"]))
        to_edit.title = request.POST["editedtitle"]
        to_edit.content = request.POST["editedcontent"]
        to_edit.save()
    except:
        pass
    concept = Concept.objects.all().order_by('id')
    return render(request, 'concept.html', locals())


def delete_concept(request):
    try:
        to_delete = Concept.objects.get(id=int(request.POST["delete_id"]))
        to_delete.delete()
    except:
        pass
    concept = Concept.objects.all().order_by('id')
    return render(request, 'concept.html', locals())

