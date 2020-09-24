from django.shortcuts import render
from django.http.response import HttpResponse
from django.template.context_processors import request

# Create your views here.

def hello_print(request):
    # 로직처리(querystring 열기, model 연동 ..)
    # 로직처리 후 화면 생성해서 return
    return HttpResponse("<h1>Hello</h1>")