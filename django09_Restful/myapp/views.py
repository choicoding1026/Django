from django.shortcuts import render

# Create your views here.
def a(request):
    
    return render(request, "a.html")

def link(request):
    
    return render(request, "link.html")

def fun1(request, name):
    print(name)
    data = {}
    data['username']=name
    return render(request, "fun1.html")

def fun2(request, year, month):
    print(year, month)
    data = {}
    data['year']=year
    data['month']=month
    return render(request, "fun2.html")

def fun3(request, yymmdd):
    print(yymmdd)
    # 날짜 타입 변경해서 처리 datetime, time
    return render(request, 'fun3.html')