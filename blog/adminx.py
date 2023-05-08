import xadmin
from xadmin import views
from .models import *
class GlobaSetting(object):
    site_title='LUIS'
    site_footer='LUIS'
    menu_style = 'accordion'
xadmin.site.register(views.CommAdminView,GlobaSetting)

class BaseSetting(object):
    enable_themes = True
    use_bootswatch = True
xadmin.site.register(views.BaseAdminView,BaseSetting)

class EntryAdminx(object):
    list_display=['title','author','visiting','category','tags','created_time','modifyed_time','hide']
    search_fields=['title']
    list_filter =['title','author']
xadmin.site.register(Entry,EntryAdminx)

class TagAdminx(object):
    list_display=['name']
    search_fields=['name']
    list_filter=['name']
xadmin.site.register(Tag,TagAdminx)

class CategoryAdminx(object):
    list_display=['name']
    search_fields = ['name']
    list_filter = ['name']
xadmin.site.register(Category,CategoryAdminx)
