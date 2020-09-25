from django.shortcuts import render

# Create your views here.
def mainM(request):
    
    return render(request, "mainM.html")

def memberAdd(request):
    print("memberAdd")
    return render(request, "b.html")

def memberDel(request):
    print("memberDel")
    return render(request, "b.html")