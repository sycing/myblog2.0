from django.shortcuts import render
from blog import models
# Create your views here.
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger

def index(request):
    # entries = models.Entry.objects.all()
    # page = request.GET.get('page', 1)
    # entry_list, paginator = make_paginator(entries, page)
    # page_data = pagination_data(paginator, page)
    return render(request, 'resource/index.html')