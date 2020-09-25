from django.shortcuts import render

# Create your views here.
def mainB(request):
    
    return render(request, "mainB.html")

def boardAdd(request):
    print("boardAdd")
    return render(request, "a.html")

def boardDel(request):
    print("boardDel")
    return render(request, "a.html")