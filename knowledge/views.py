from django.shortcuts import render,redirect
from knowledge.models import Concept, Relation, ToLink, ForthLink
# Create your views here.

# Concept Part


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


#  Relation Part


def relation_view(request):

    # Visual Collect
    relation = Relation.objects.all().order_by('id')
    return render(request, 'relation.html', locals())


def create_relation(request):
    # Function Part
    rr = Relation.objects.create(title=request.POST["new_relation_title"],
                                 content=request.POST["new_relation_content"],
                                 color=request.POST["new_relation_color"])

    # Visual Collect
    relation = Relation.objects.all().order_by('id')
    return render(request, 'relation.html', locals())


def edit_relation(request):
    # Function Part
    edit_relation_id = request.POST["edit_relation_id"]

    # Visual Collect
    relation = Relation.objects.all().order_by('id')
    return render(request, 'relation.html', locals())


def edit_relation_save(request):
    # Function Part
    try:
        to_edit_relation = Relation.objects.get(id=int(request.POST["to_edit_relation"]))
        to_edit_relation.title = request.POST["edited_relation_title"]
        to_edit_relation.content = request.POST["edited_relation_content"]
        to_edit_relation.color = request.POST["edited_relation_color"]
        to_edit_relation.save()
    except:
        pass

    # Visual Collect
    relation = Relation.objects.all().order_by('id')
    return render(request, 'relation.html', locals())


def delete_relation(request):
    # Function Part
    try:
        to_delete_relation = Relation.objects.get(id=int(request.POST["delete_relation_id"]))
        to_delete_relation.delete()
    except:
        pass

    # Visual Collect
    relation = Relation.objects.all().order_by('id')
    return render(request, 'relation.html', locals())
