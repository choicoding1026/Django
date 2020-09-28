from django.shortcuts import render, redirect
from myapp.models import Product
from django.http.response import HttpResponseRedirect
from django.views.generic.list import ListView
from django.views.generic.base import View
from django.views.generic.detail import DetailView

# Create your views here.
def model(request):
    
    return render(request, "model.html")
###############################################################################
#def list(request):
#    
#    productList = Product.objects.all().order_by("-code") # -code 내림차순 #(1)
#    # select * from product
#    
#    return render(request, "list.html" #(2)
#                  , {"productlist":productList}) #(3)
class ProductListCBV(ListView):
    
    model = Product #(1)
    template_name = "list.html" #(2)
    context_object_name = "productlist" #(3)
################################################################################
#def write(request):
#    
#        code = request.POST.get("code")
#        name = request.POST.get("name")
#        price = request.POST.get("price")
#        
#        # DB에 저장
#        Product(code=code, name=name, price=price).save()
#        
#        return HttpResponseRedirect("/main/list")
class ProductWriteCBV(View):
    def post(self, request):
        
        code = request.POST.get("code")
        name = request.POST.get("name")
        price = request.POST.get("price")
        
        # DB에 저장
        Product(code=code, name=name, price=price).save()
        # insert into product (code, name, price)
        # values (code, name, price)
        return HttpResponseRedirect("/main/list")
    def get(self, request):
        pass
################################################################################    
#def writeForm(request):
#    
#    return render(request, "writeForm.html")   
################################################################################ 
#def detail(request, code):
#    
#    result = Product.objects.get(code=code) #(1)
#    # select * from product where code=code
#    product={}
#    product['code']=result.code
#    product['name']=result.name
#    product['price']=result.price
#    product['pub_date']=result.pub_date
#    
#    return render(request, "detail.html" #(2)
#                  , product) #(3)
class ProductDetailCBV(DetailView):
    
    model = Product #(1)
    template_name = "detail.html" #(2)
    context_object_name = "product" #(3)
    # URL에서 pk값을 전송해야한다.
    # path('detail/<str:pk', views.ProductDetailCBV.as_view(), name="detail_product")
################################################################################
#def delete(request):
#    
#    code = request.GET.get("code")
#    
#    result = Product.objects.get(code=code)
#    result.delete()
#    # delete from product where code=code
#    
#    return redirect("/main/list")
#    # return HttpResponseRedirect("/main/list")
class ProductDeleteCBV(View):
    
    def get(self, request):
        code = request.GET.get("code")
    
        result = Product.objects.get(code=code)
        result.delete()
        # delete from product where code=code
    
        return redirect("/main/list")
################################################################################    
#def update(request):
#    
#    code = request.POST.get("code")
#    name = request.POST.get("name")
#    price = request.POST.get("price")
#        
#    result = Product.objects.get(code=code)
#    result.name = name
#    result.price = price
#    result.save()
#        
#    return redirect("/main/list")
class ProductUpdateCBV(View):
    
    def post(self, request):
        code = request.POST.get("code")
        name = request.POST.get("name")
        price = request.POST.get("price")
        
        result = Product.objects.get(code=code)
        result.name = name
        result.price = price
        result.save()
        
        return redirect("/main/list")
################################################################################