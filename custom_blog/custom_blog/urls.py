# -*- coding: utf-8 -*-

from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
#from article.views import RSSFeed

urlpatterns = patterns('',
                        # Examples:
                        # url(r'^$', 'my_blog.views.home', name='home'),
                        # url(r'^blog/', include('blog.urls')),
                        url(r'^(?P<id>\d+/$)', 'article.views.detail', name = 'detail'), 
                        url(r'^admin/', include(admin.site.urls)),
                        url(r'^$', 'article.views.home', name = 'home'), 
                        url(r'^coding/$', 'article.views.coding', name = 'coding'),
                        url(r'^home/$', 'article.views.home', name = 'home'),
                        url(r'^thought/$', 'article.views.thought', name = 'thought'),
                        url(r'^wonderful_life/$', 'article.views.wonderful_life', name = 'wonderful_life'),
                        url(r'^manage/$', 'article.views.manage', name = 'manage'),
                        url(r'^coding/show_article/$', 'article.views.show_article', name = 'show_article'),
                      )
if settings.DEBUG:  
    urlpatterns += patterns('',  
            (r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_PATH, 'show_indexes':True}),  
            )
