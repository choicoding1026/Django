from django.shortcuts import render
from django.http.response import HttpResponseRedirect

# Create your views here.
def session(request):
    
    return render(request, "session.html")

def loginForm(request):
    
    return render(request, "loginForm.html")

def login(request):
    
    userId = request.GET.get("userId")
    userPw = request.GET.get("userPw")
    # DB 연동해서 ID/PW 검사 필요
    
    # 필요한 데이터를 서버 메모리인 세션에 저장
    # 문법: request.session[key]=value
    request.session['userId']=userId
    # terminal 접속 후 python manage.py migrate 후 실행
    return render(request, "login.html")

def loginInfo(request):
    #로그인 처리 여부 확인
    if 'userId' in request.session:
        print(request.session.keys())
        print(request.session.items())
        print(request.session.get('userId'))
        return render(request, "loginInfo.html")
    else:
        return HttpResponseRedirect("/main/loginForm")
    
def logOut(request):
    
    if 'userId' in request.session:
        request.session.flush()
        return render(request, "logOut.html")
    else:
        return HttpResponseRedirect("/main/loginForm")
