from django.conf.urls import url
from . import views
from django.urls import path, re_path, include
from django.views.generic import TemplateView #处理静态文件




app_name = 'blog'

urlpatterns = [
    re_path('^$', views.index,name='blog_index'),
    re_path(r'^(?P<blog_id>[0-9]+)/$', views.detail,name='blog_detail'),
    re_path(r'^category/(?P<category_id>[0-9]+)/$', views.CatagoryOldView, name='blog_category'),
    re_path(r'^tag/(?P<tag_id>[0-9]+)/$', views.tag,name='blog_tag'),
    re_path (r'^search/$', views.search,name='blog_search'),
    re_path(r'^archives/(?P<year>[0-9]+)/(?P<month>[0-9]+)$', views.archives, name='blog_archives'),
    re_path(r'^reply/(?P<comment_id>\d+)/$', views.reply, name='comment_reply'),
    # path(r'logincheck/',views.user_login)
    path(r'login/',views.LoginVeiw.as_view()),
    path(r'loginout/',views.log_out),
    path('api-auth/', include('rest_framework.urls'))
]