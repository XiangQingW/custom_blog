# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse
from article.models import Article
from django.http import Http404

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


# Create your views here.

def home(request):
    post_list = Article.objects.all()  #获取全部的Article对象
    return render(request, 'home.html', {'post_list' : post_list})

def hello_world(request):
    return HttpResponse("Hello World!")

def detail(request, id):
    try:
        post = Article.objects.get(id = str(id[0]))
    except Article.DoesNotExit:
        raise Http404
    return HttpResponse(request, 'post.html', {'post':post})
