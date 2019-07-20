"""website URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,re_path
from django.conf.urls import include
from django.conf import settings
from django.conf.urls.static import static
from blog.feed import LatestEntriesFeed
from blog import views as blog_views
from django.contrib.sitemaps import GenericSitemap
from django.contrib.sitemaps.views import sitemap
from blog.models import Entry

from django.views import static as views_static
from django.conf.urls import url ##新增

import xadmin

handler403 = 'blog.views.permission_denied'
handler404 = 'blog.views.page_not_found'
handler500 = 'blog.views.page_error'

info_dict = {
    'queryset': Entry.objects.all(),
    'date_field': 'modifyed_time'
}

urlpatterns = [
    re_path(r'^$',blog_views.index),
    path('admin/', admin.site.urls),
    # path('xadmin/',xadmin.site.urls),
    re_path(r'^blog/', include('blog.urls')),
    re_path(r'^latest/feed/$', LatestEntriesFeed()),    #RSS订阅
    re_path(r'^sitemap\.xml$', sitemap, {'sitemaps': {'blog': GenericSitemap(info_dict, priority=0.6)}},
      name='django.contrib.sitemaps.views.sitemap'),       #站点地图
    re_path(r'^comments/', include('django_comments.urls')),
    re_path(r'^login/$', blog_views.login),
    re_path(r'^logout/$', blog_views.logout),

    ##加载静态图片写法1
    # url(r'^static/(?P<path>.*)$', views_static.serve,
    #   {'document_root': settings.STATIC_ROOT}, name='static'),

    #加载静态图片写法2
    # url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
    # url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),

    #加载静态较图片写法3
    url(r'^static/(?P<path>.*)$', views_static.serve, {'document_root': settings.STATIC_ROOT}, name='media'),
    url(r'^media/(?P<path>.*)$', views_static.serve, {'document_root': settings.MEDIA_ROOT}, name='media'),
]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT )#添加图片的url


