#_*_coding:utf-8_*_
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, 'blog/index.html', context={
                    'title': '触手可及', 
                    'welcome': 'Welcome to my blog'
                })
