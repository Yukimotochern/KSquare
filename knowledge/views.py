from django.shortcuts import render,redirect, get_object_or_404
from django.db import transaction
from knowledge.models import Concept, Relation, ToLink, ForthLink
from knowledge.models import get_or_create_by_title
from django.core.exceptions import ObjectDoesNotExist
from django.http import JsonResponse
from knowledge.treeview import TreeViewModel

# Create your views here.

# Concept Part


def concept_view(request):
    concept = Concept.objects.all().order_by('id').reverse()
    return render(request, 'concept.html', locals())


def create_concept(request):
    dd = Concept.objects.create(title=request.POST["newtitle"], content=request.POST["newcontent"])
    concept = Concept.objects.all().order_by('id').reverse()
    return render(request, 'concept.html', locals())


def edit_concept(request):
    edit_id = request.POST["edit_id"]
    concept = Concept.objects.all().order_by('id').reverse()
    return render(request, 'concept.html', locals())


def edit_concept_save(request):
    try:
        to_edit = Concept.objects.get(id=int(request.POST["toedit"]))
        to_edit.title = request.POST["editedtitle"]
        to_edit.content = request.POST["editedcontent"]
        to_edit.save()
    except:
        pass
    concept = Concept.objects.all().order_by('id').reverse()
    return render(request, 'concept.html', locals())


def delete_concept(request):
    try:
        to_delete = Concept.objects.get(id=int(request.POST["delete_id"]))
        to_delete.delete()
    except:
        pass
    concept = Concept.objects.all().order_by('id').reverse()
    return render(request, 'concept.html', locals())


#  Relation Part


def relation_view(request):

    # Visual Collect
    to_link = ToLink.objects.all().order_by('id').reverse()
    forth_link = ForthLink.objects.all().order_by('id').reverse()
    concept = Concept.objects.all().order_by('id').reverse()
    relation = Relation.objects.all().order_by('id').reverse()
    return render(request, 'relation.html', locals())


def create_relation(request):
    # Function Part
    rr = Relation.objects.create(title=request.POST["new_relation_title"],
                                 content=request.POST["new_relation_content"],
                                 color=request.POST["new_relation_color"],
                                 t_is_f=request.POST["new_t_is_f"],
                                 f_is_t=request.POST["new_f_is_t"])

    # Visual Collect
    to_link = ToLink.objects.all().order_by('id').reverse()
    forth_link = ForthLink.objects.all().order_by('id').reverse()
    concept = Concept.objects.all().order_by('id').reverse()
    relation = Relation.objects.all().order_by('id').reverse()
    return render(request, 'relation.html', locals())


def edit_relation(request):
    # Function Part
    edit_view = True
    edit_relation_id = request.POST["edit_relation_id"]

    # Visual Collect
    to_link = ToLink.objects.all().order_by('id').reverse()
    forth_link = ForthLink.objects.all().order_by('id').reverse()
    concept = Concept.objects.all().order_by('id').reverse()
    relation = Relation.objects.all().order_by('id').reverse()
    return render(request, 'relation.html', locals())


def edit_relation_save(request):
    # Function Part
    try:
        to_edit_relation = Relation.objects.get(id=int(request.POST["to_edit_relation"]))
        to_edit_relation.title = request.POST["edited_relation_title"]
        to_edit_relation.content = request.POST["edited_relation_content"]
        to_edit_relation.color = request.POST["edited_relation_color"]
        to_edit_relation.t_is_f = request.POST["edited_t_is_f"]
        to_edit_relation.f_is_t = request.POST["edited_f_is_t"]
        to_edit_relation.save()
    except:
        pass

    # Visual Collect
    to_link = ToLink.objects.all().order_by('id').reverse()
    forth_link = ForthLink.objects.all().order_by('id').reverse()
    concept = Concept.objects.all().order_by('id').reverse()
    relation = Relation.objects.all().order_by('id').reverse()
    return render(request, 'relation.html', locals())


def delete_relation(request):
    # Function Part
    try:
        to_delete_relation = Relation.objects.get(id=int(request.POST["delete_relation_id"]))
        to_delete_relation.delete()
    except:
        pass

    # Visual Collect
    to_link = ToLink.objects.all().order_by('id').reverse()
    forth_link = ForthLink.objects.all().order_by('id').reverse()
    concept = Concept.objects.all().order_by('id').reverse()
    relation = Relation.objects.all().order_by('id').reverse()
    return render(request, 'relation.html', locals())


# Link Part
@transaction.atomic
def create_link(request):
    # Find the 'to' concept objects if no create one
    to_concept = get_or_create_by_title(Concept, request.POST["new_to_concept_title"])
    # Find the 'forth' concept objects if no create one
    forth_concept = get_or_create_by_title(Concept, request.POST["new_forth_concept_title"])
    # Find the 'relation' objects if no create one
    link_relation = get_or_create_by_title(Relation, request.POST["new_link_relation_title"])
    # Create 'to' object
    to_link_ob = ToLink.objects.create(relation_main=link_relation, related_concept=to_concept)
    # Create 'forth' object
    forth_link_ob = ForthLink.objects.create(relation_main=link_relation, related_concept=forth_concept,
                                             to_link_partner=to_link_ob)

    # Visual Collect
    to_link = ToLink.objects.all().order_by('id').reverse()
    forth_link = ForthLink.objects.all().order_by('id').reverse()
    concept = Concept.objects.all().order_by('id').reverse()
    relation = Relation.objects.all().order_by('id').reverse()
    return render(request, 'relation.html', locals())


def edit_link(request):
    edit_link_view = True
    edit_link_id = request.POST["edit_link_id"]

    # Visual Collect
    to_link = ToLink.objects.all().order_by('id').reverse()
    forth_link = ForthLink.objects.all().order_by('id').reverse()
    concept = Concept.objects.all().order_by('id').reverse()
    relation = Relation.objects.all().order_by('id').reverse()
    return render(request, 'relation.html', locals())


def edit_link_save(request):
    # Function Part
    try:
        to_edit_link = ToLink.objects.get(id=int(request.POST["edited_link_id"]))
        to_edit_link.related_concept = get_or_create_by_title(Concept, request.POST["edited_to_title"])
        to_edit_link.forth_link_partner.related_concept = get_or_create_by_title(Concept,
                                                                                 request.POST["edited_forth_title"])
        to_edit_link.forth_link_partner.save()
        to_edit_link.save()
    except ObjectDoesNotExist:
        pass

    # Visual Collect
    to_link = ToLink.objects.all().order_by('id').reverse()
    forth_link = ForthLink.objects.all().order_by('id').reverse()
    concept = Concept.objects.all().order_by('id').reverse()
    relation = Relation.objects.all().order_by('id').reverse()
    return render(request, 'relation.html', locals())


def delete_link(request):
    # Function Part
    try:
        to_delete_link = ToLink.objects.get(id=int(request.POST["delete_link_id"]))
        to_delete_link.delete()
    except ObjectDoesNotExist:
        pass
    # Visual Collect
    to_link = ToLink.objects.all().order_by('id').reverse()
    forth_link = ForthLink.objects.all().order_by('id').reverse()
    concept = Concept.objects.all().order_by('id').reverse()
    relation = Relation.objects.all().order_by('id').reverse()
    print(len(to_link) == len(forth_link))
    return render(request, 'relation.html', locals())


def find_to_name(request):
    cur_title = request.GET['current_new_link_relation_title']
    try:
        ti = Relation.objects.get(_title=cur_title)
    except Relation.DoesNotExist:
        ti = None
    if ti is None:
        t_is_f = "尚未建立"
    else:
        t_is_f = ti.t_is_f
    sent_dict = {"t_is_f": t_is_f}
    return JsonResponse(sent_dict)


#  Tree Explore Part


def tree(request, main_view_id):
    main_model_concept = get_object_or_404(Concept, id=main_view_id)
    typ = type(main_model_concept)
    tree_view_model = TreeViewModel(main_model_concept)
    positioned_page = TreeViewModel.positioning(tree_view_model.tree_cell_page)
    return render(request, 'square_tree.html', locals())


def all_concepts(request):
    concepts = Concept.objects.all()
    return render(request, 'total_explore.html', locals())




















