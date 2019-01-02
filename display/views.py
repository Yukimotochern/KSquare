from django.shortcuts import render, redirect, reverse
from knowledge.models import Concept
from django.views.generic import ListView, View

# Create your views here.


def search_index(request):
    index_concept = Concept.objects.all()[:9]
    hot_concept = Concept.objects.all()[:8]
    history_concept = Concept.objects.all()[:8]
    new_concept = Concept.objects.all()[:8]
    recommend_concept = Concept.objects.all()[:8]
    attention_concept = Concept.objects.all()[:8]
    context = {
        'first_index_concept': index_concept[:3],
        'second_index_concept': index_concept[3:6],
        'third_index_concept': index_concept[6:],
        'hot_concept': hot_concept,
        'history_concept': history_concept,
        'new_concept': new_concept,
        'recommend_concept': recommend_concept,
        'attention_concept': attention_concept,
        'kaishi': [1, 4, 7, 10],
        'jiewei': [3, 6, 9, 12],
    }
    return render(request, 'outter/search2.html', context=context)


def tag_view(request, tag_id):
    tag = Concept.objects.get(id=tag_id)

    return render(request,'outter/tag_view.html',context={'tag':tag})


# def search_result(request):
    # search_name=request.GET.get("search")
    # result=Concept.objects.filter(_title__exact=search_name)
    # if result.count() == 0:
    #     result=Concept.objects.filter(_title__contains=search_name)
    #     if result.count() == 0:
    #         return render(request,'search_result.html',context={
    #             'text': "对不起，没有搜索到您想要的结果",
    #             'result': result
    #         })
    #     else:
    #         return render(request, 'search_result.html', context={
    #             'text': "没有搜到 " + search_name + " ,包含 " + request.GET.get("search") + " 的结果有" + str(result.count()) + "条。",
    #             'result': result
    #         })
    # elif result.count() == 1:
    #     id = result.first().id
    #     return redirect(reverse("TagView",kwargs={'tag_id':id}))
    # else:
    #     return render(request, 'search_result.html', context={
    #         'text': "搜索到"+result.count()+"条结果",
    #         'result': result
    #     })


class ArticleListView(ListView, View):
    model = Concept
    template_name = 'outter/search_result.html'
    context_object_name = 'concepts'
    paginate_by = 10
    ordering = 'create_time'
    page_kwarg = 'p'

    def get_context_data(self, **kwargs):
        context = super(ArticleListView, self).get_context_data(*kwargs)
        paginator = context.get('paginator')
        page_obj = context.get('page_obj')
        pagination_data = self.get_pagination_data(paginator, page_obj, 3)
        context.update(pagination_data)
        text = ''
        search_name = self.request.GET.get("result")
        if search_name is None:
            contepts = Concept.objects.filter(_title__contains=search_name)
            if contepts:
                text = '搜索到' + str(contepts.count()) + '条结果'
            else:
                text = '对不起，没有搜索到结果'

        context['text']=text
        context['search_name'] = search_name
        return context

    def get_pagination_data(self, paginator, page_obj, around_count=2):
        current_page = page_obj.number
        num_pages = paginator.num_pages

        left_has_more = False
        right_has_more = False

        if current_page <= around_count + 2:
            left_pages = range(1,current_page)
        else:
            left_has_more = True
            left_pages = range(current_page-around_count,current_page)

        if current_page >= num_pages - around_count - 1:
            right_pages = range(current_page+1, num_pages+1)
        else:
            right_has_more = True
            right_pages = range(current_page+1, current_page+around_count+1)

        return {
            'left_pages': left_pages,
            'right_pages': right_pages,
            'current_page': current_page,
            'left_has_more': left_has_more,
            'right_has_more': right_has_more,
            'num_pages': num_pages
        }

    def get_queryset(self):
        search_name = self.request.GET.get("result")
        if search_name:
            return Concept.objects.filter(_title__icontains=search_name)
        else:
            return Concept.objects.all()

