from django.shortcuts import render
from django.http.response import HttpResponse
from django.template.context_processors import request

# Create your views here.

def hello_print(request):
    # ����ó��(querystring ����, model ���� ..)
    # ����ó�� �� ȭ�� �����ؼ� return
    return HttpResponse("<h1>Hello</h1>")