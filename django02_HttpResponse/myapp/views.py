from django.shortcuts import render

# Create your views here.
'''
   views.py의 함수가 처리하는 핵심 작업 2가지
   1. 비즈니스 로직처리 
   2. 화면생성 ( Template 생성, html 생성 )
     따라서  'return 값' 형태로 사용된다. 
     
     가. return HttpResponse("html코드")
     나. return render( request   , "html파일"   )  
'''
from django.http.response import HttpResponse

def delBoard(request):
    print(request) # WSGIRequest 클래스

    return HttpResponse("<p>Hello World, delete</p>")


def updateBoard(request):
    return HttpResponse("<p>Hello World, update</p>")

def selectBoard(request):
    return HttpResponse("<p>Hello World, select</p>")






