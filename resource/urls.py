from django.conf.urls import url
from . import views
from django.urls import path,re_path
from django.views.generic import TemplateView #处理静态文件

app_name = 'resource'
urlpatterns = [
    re_path('^$', views.index,name='content'),
    re_path(r'^upload/$', views.upload,name='upload'),
    re_path(r'^test$', views.test,name='test'),

]