from django.shortcuts import render

# Create your views here.
def memberInsert(request):
    print("memberInsert")
    return render(request, "a.html")

def memberDelete(request):
    print("memberDelete")
    return render(request, "a.html")

def link(request):
    return render(request, "link.html")