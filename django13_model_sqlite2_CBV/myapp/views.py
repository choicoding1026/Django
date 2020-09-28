from django.shortcuts import render, redirect
from myapp.models import Product
from django.http.response import HttpResponseRedirect
from django.views.generic.list import ListView
from django.views.generic.base import View
from django.views.generic.detail import DetailView
from itertools import product

# Create your views here.
def model(request):
    
    return render(request, "model.html")

##########################################################################
# 목록보기 : select
# 1. Function-Based Views
# def list(request):
#    
#    # productList = Product.objects.all().order_by("-code") # -code 내림차순
#    productList = Product.objects.all()
#    # select * from product
#    
#    return render(request, "list.html", {"productlist":productList})
# 2. Class-Based Views(CBV)
# class ProductList(ListView):
#    
#    model = Product
#    template_name = "list.html"
#    context_object_name = "productlist"
# 3. Class-Based Views(CBV) - select 시  커스터마이징 가동    
class ProductList(ListView):
    
    model = Product
    template_name = "list.html"
    context_object_name = "productlist"
    
    def get_queryset(self):
        return Product.objects.all().order_by("-code")
##########################################################################    
# 1. FBV
# def write(request):
#    
#    if request.method == "POST":
#        
#        code = request.POST.get("code")
#        name = request.POST.get("name")
#        price = request.POST.get("price")
#        
#        # DB에 저장
#        Product(code=code, name=name, price=price).save()
#        
#        return HttpResponseRedirect("/main/list")
#    else:
#        
#        return render(request, "writeForm.html")
#    
# 2. CBV
class WriteCBV(View):
    
    def post(self, request):
        
        code = request.POST.get("code")
        name = request.POST.get("name")
        price = request.POST.get("price")
        
        # DB에 저장
        Product(code=code, name=name, price=price).save()
        
        return HttpResponseRedirect("/main/list")
##########################################################################     
# 1. FBV
# def detail(request, code):
#    
#    result = Product.objects.get(code=code)
#    # select * from product where code=code
#    product={}
#    product['code']=result.code
#    product['name']=result.name
#    product['price']=result.price
#    product['pub_date']=result.pub_date
#    
#    return render(request, "detail.html", product)
# 2. CBV
class DetailCBV(DetailView):

    model = Product
    template_name = "detail.html"
    context_object_name = "goods"

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