from django.shortcuts import render, redirect
from myapp.models import Product
from django.http.response import HttpResponseRedirect

# Create your views here.
def model(request):
    
    return render(request, "model.html")

def list(request):
    
    productList = Product.objects.all().order_by("-code") # -code 내림차순
    # select * from product
    
    return render(request, "list.html", {"productlist":productList})

def write(request):
    
        code = request.POST.get("code")
        name = request.POST.get("name")
        price = request.POST.get("price")
        
        # DB에 저장
        Product(code=code, name=name, price=price).save()
        
        return HttpResponseRedirect("/main/list")
    
def writeForm(request):
    
    return render(request, "writeForm.html")   
 
def detail(request, code):
    
    result = Product.objects.get(code=code)
    # select * from product where code=code
    product={}
    product['code']=result.code
    product['name']=result.name
    product['price']=result.price
    product['pub_date']=result.pub_date
    
    return render(request, "detail.html", product)

def delete(request):
    
    code = request.GET.get("code")
    
    result = Product.objects.get(code=code)
    result.delete()
    # delete from product where code=code
    
    return redirect("/main/list")
    # return HttpResponseRedirect("/main/list")
    
def update(request):
    
    code = request.POST.get("code")
    name = request.POST.get("name")
    price = request.POST.get("price")
        
    result = Product.objects.get(code=code)
    result.name = name
    result.price = price
    result.save()
        
    return redirect("/main/list")