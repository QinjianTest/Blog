from django.shortcuts import render
from BlogV1.models import *
from django.db.models import Q
from lib.pagination import Pagination


# Create your views here.

def index(request):
    article_list = Articles.objects.filter(status=1).order_by('-change_date')
    tech_list = Articles.objects.filter(Q(category=1)&Q(recommend=1)).order_by('-change_date')[:6]
    life_list = Articles.objects.filter(Q(category=2)&Q(recommend=1)).order_by('-change_date')[:6]

    query_params = request.GET.copy()
    pager = Pagination(
        current_page=request.GET.get('page'),
        all_count=article_list.count(),
        base_url=request.path_info,
        query_params=query_params,
        per_page=5,
        pager_page_count=7
    )
    # 文章列表
    article_list = article_list[pager.start:pager.end]

    return render(request,'index.html',locals())

def article(request,nid):
    article_query = Articles.objects.filter(nid=nid)
    if not article_query:
        return redirect('/')
    article = article_query.first()
    return render(request, 'article.html',locals())

def tech(request):
    article_list = Articles.objects.filter(status=1).order_by('-change_date')

    query_params = request.GET.copy()
    pager = Pagination(
        current_page=request.GET.get('page'),
        all_count=article_list.count(),
        base_url=request.path_info,
        query_params=query_params,
        per_page=5,
        pager_page_count=7
    )
    # 文章列表
    article_list = article_list[pager.start:pager.end]
    return render(request, 'tech.html',locals())

def testxmind(request):
    return render(request, 'testxmind.html')

def life(request):
    return render(request, 'life.html')

def about(request):
    return render(request, 'about.html')
