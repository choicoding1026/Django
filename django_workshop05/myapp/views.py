from django.shortcuts import render
from django.http.response import HttpResponseRedirect

# Create your views here.
data = [{"username":"홍길동","age":20,"address":"서울","email":"aaa254@gmail.com"},
    {"username":"이순신","age":30,"address":"경기","email":"bbb.lee@gmail.com"},
    {"username":"유관순","age":40,"address":"부산","email":"ccc@gmail.com"},
    {"username":"강감찬","age":50,"address":"광주","email":"ddd.kang@gmail.com"},
    {"username":"세종","age":70,"address":"서울","email":"eee@gmail.com"},
    {"username":"세종대왕","age":83,"address":"제주","email":"fff@gmail.com"},
    {"username":"윤봉길","age":34,"address":"강원","email":"ggg@gmail.com"},]
    
def list(request):
    # 문자열 형태의  json형식의 리스트인 경우: json.loads(data)
    return render(request, "list.html" , {"list":data})

def detail(request):
    
    email = request.GET.get("email")
    print(email)
    user = {}
    for p in data:
        if p['email'] == email:
            user = p
    print(user)
    return render(request, "detail.html", user)

def memberForm(request):

    return render(request, "memberForm.html" )

def add(request):
    
    email = request.POST.get("email")
    username = request.POST.get("username")
    age = request.POST.get("age")
    address = request.POST.get("address")
    
    user = {}
    user['email'] = email
    user['username'] = username
    user['age'] = age
    user['address'] = address
    
    data.append(user)
    
    return HttpResponseRedirect("/main/list")
