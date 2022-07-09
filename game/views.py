from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def index(resquest):
    return HttpResponse("我的第一个网页！！！！")