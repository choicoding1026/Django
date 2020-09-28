from django.shortcuts import render
from django.http.response import HttpResponseRedirect

# Create your views here.
def cookie(request):
    
    return render(request, "cookie.html")

def loginForm(request):
    
    return render(request, "loginForm.html")

def login(request):
    
    userId = request.GET.get("userId")
    userPw = request.GET.get("userPw")
    # DB 연동해서 ID/PW 검사 필요
    
    # 필요한 데이터를 클라이언트(브라우저)에 저장
    response = render(request, 'login.html')
    response.set_cookie("userId", userId, 3600)
    return response

def loginInfo(request):
    #로그인 처리 여부 확인
    userId = request.COOKIES.get("userId")
    if userId:
        return render(request, "loginInfo.html")
    else:
        return HttpResponseRedirect("/main/loginForm")
    
def logOut(request):
    
    userId = request.COOKIES.get("userId")
    if userId:
        response = render(request, 'logOut.html')
        response.delete_cookie("userId")
        return response
    else:
        return HttpResponseRedirect("/main/loginForm")