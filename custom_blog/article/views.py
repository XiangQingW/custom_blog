# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from article.models import Article

# Create your views here.

def home(request):
        posts = Article.objects.all()  #获取全部的Article对象
        paginator = Paginator(posts, 2) #每页显示两个
        page = request.GET.get('page')
        try :
            post_list = paginator.page(page)
        except PageNotAnInteger :
            post_list = paginator.page(1)
        except EmptyPage :
            post_list = paginator.paginator(paginator.num_pages)
        return render(request, 'home.html', {'post_list' : post_list})

