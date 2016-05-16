# -*- coding: utf-8 -*-
from django.http import HttpResponse
from article.models import Article
from article.models import BlogDatabase
from django.http import Http404
from django.template.loader import get_template
from django import template
import time


# Create your views here.

def current_time():
    return time.strftime('%Y-%m-%d %X',time.localtime(time.time()))


def home(request):
    t = get_template('home.html')
    html = t.render()
    return HttpResponse(html)

def detail(request, id):
    try:
        post = Article.objects.get(id = str(id[0]))
    except Article.DoesNotExit:
        raise Http404
    return HttpResponse(request, 'post.html', {'post':post})

def wonderful_life(request):
    print('I am running')
    t = get_template('wonderful_life.html')
    html = t.render()
    return HttpResponse(html)

def coding(request):
    articles = BlogDatabase.objects.all()
    t = get_template('coding.html')
    c = template.Context({'articles':articles})
    html = t.render(c)
    return HttpResponse(html)

def thought(request):
    t = get_template('thought.html')
    html = t.render()
    return HttpResponse(html)

def manage(request):
    t = get_template('manage.html')
    html = t.render()
    return HttpResponse(html)

def show_article(request):
    full_path = request.get_full_path()
    article_id = int(full_path.split('/')[2])
    article_fill = BlogDatabase.objects.get(id=article_id)
    t = get_template('show_article.html')
    c = template.Context({'article_fill':article_fill})
    html = t.render(c)
    return HttpResponse(html)
