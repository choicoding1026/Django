from django.shortcuts import render


# Create your views here.

def template_a2(request):
    username = "홍길동"   # 로컬변수
    age = 20
    return render(request, "template_a.html", 
                  {"username_key":username,"age_key":age})
    
def template_a(request):
    username = "홍길동2"   # 로컬변수
    age = 40
    
    data={}
    data['username_key']=username
    data['age_key']=age
    print(data)
    return render(request, "template_a.html", data)

#######################################################
class User:
    
    def __init__(self, username, age):
        self.username = username
        self.age = age
        
    def _str__(self): # 매직 함수(메서드)
        return self.username +"\t" + str(self.age)
        
def template_b(request):

    user1 = User("유관순", 20)
    data = {}
    data['user01_key']=user1
    return render(request, "template_b.html", data)

def template_c(request):
    name_list=["이순신","유관순","강감찬","정조","세종"]
    data ={}
    data['name_list']=name_list
    return render(request, "template_c.html", data)

def template_d(request):
    user_list=[User("유관순", 20),User("이순신", 44),User("강감찬", 40)]
    data ={}
    data['user_list']=user_list
    return render(request, "template_d.html", data)

#############################################
def template_e(request):
    
    dict_value = {"prod_name":"핸드폰","price":130}
    
    dict_list=[{"prod_name":"노트북","price":230},
                {"prod_name":"냉장고","price":130},
                {"prod_name":"TV","price":90}]
    
    data = {}
    data['dict_list']=dict_list
    data['dict_value']=dict_value
    
    return render(request, "template_e.html", data)

############################################
def template_f(request):
    username = "홍길동"   
    age = 20
    
    data={}
    data['username']=username
    data['age']=age
    
    return render(request, "template_f.html", data)

###################################################
from datetime import datetime
def template_g(request):
    mesg = "hello World Happy"
    v_list = ['AAA','BBB','CCC']
    data={}
    data['mesg']=mesg
    data['v_list']=v_list
    data['number']=10
    
#     x = [10, 20 ,30]
#     y = [1, 2, 3]
#     print(x+y)  # numpy는 벡터연산 가능하다. [11, 22, 33] 
    
    currentDate = datetime.now()
    data['currentDate']=currentDate
    
    # CSS
    some_list=['AAA','BBB','CCC','DDD','EEE','FFF','GGG']
    data['some_list']=some_list

    # dictsort
    p_list =[
    {'name': 'zed', 'age': 19},
    {'name': 'amy', 'age': 22},
    {'name': 'joe', 'age': 31},
    ]
    data['p_list']=p_list

    return render(request, "template_g_filter.html",
                  data)







