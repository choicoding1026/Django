from django.shortcuts import render
from django.http.response import HttpResponse, HttpResponseRedirect

# Create your views here.

# 직적 HttpResponse 객체 이용해서 HTML 적용
def a(request):
    
    return HttpResponse("<p>HTML 직접 작성, HttpResponse")

# render 함수 이용해서 외부 html 지정
def b(request):
    
    return render(request, "b.html")

def c(request):
    
    return HttpResponseRedirect("/main/a") # 재요청 하고싶은 경로