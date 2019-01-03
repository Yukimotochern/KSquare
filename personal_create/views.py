from django.shortcuts import render
from knowledge.models import Concept, Link, Relation, ToLink, ForthLink, get_or_create_by_title
from django.http import JsonResponse
from django import utils
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from personal_create.create import TxtParser
from tagging.models import Tag

# Create your views here.


@login_required
def fields(request, tab):
    tab = tab
    return render(request, 'personal/create/fields.html', locals())


@login_required
def concepts(request, tab):
    tab = tab
    all_concepts = Concept.objects.filter(owner=request.user).order_by('id').reverse()
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


@login_required
def templates(request, tab):
    tab = tab
    if request.method == 'POST':
        try:
            # text_correct = 'try: #tt\n\t@uu:\n\t\ty\n\t\ti\n\tlalalala'
            text = request.POST['document_content'].replace('\r\n', '\n')
            # for i in range(len(text)):
            #     if text_correct[i] != text[i]:
            #         print(f"{text[i]}->{i}", '\nGG')
            # print(text_correct == text)
            parser = TxtParser(text)
            result = parser.parse()
            concepts_list = result[0]
            links_list = result[1]
            for link in links_list:
                concept1 = get_or_create_by_title(Concept, link.title1)
                concept1.owner = request.user
                concept1.save()
                concept2 = get_or_create_by_title(Concept, link.title2)
                concept2.owner = request.user
                concept2.save()
                relation_to_link = get_or_create_by_title(Relation, link.relation)
                relation_to_link.t_is_f = ""
                relation_to_link.f_is_t = ""
                relation_to_link.save()
                forth_link = ForthLink.objects.create()
                forth_link.relation_main = relation_to_link
                forth_link.related_concept = concept1
                to_link = ToLink.objects.create()
                to_link.related_concept = concept2
                to_link.relation_main = relation_to_link
                forth_link.to_link_partner = to_link
                forth_link.save()
                to_link.save()
            for concept in concepts_list:
                ob = get_or_create_by_title(Concept, concept.title)
                ob.owner = request.user
                ob.summary = concept.summary
                if concept.tags:
                    Tag.objects.update_tags(ob, " ".join(concept.tags))
                ob.save()

        except EOFError:
            pass
    # Visual Collect
    to_link = ToLink.objects.all().order_by('id').reverse()
    forth_link = ForthLink.objects.all().order_by('id').reverse()
    concept = Concept.objects.filter(owner=request.user).order_by('id').reverse()
    relation = Relation.objects.all().order_by('id').reverse()
    return render(request, 'personal/create/templates.html', locals())











