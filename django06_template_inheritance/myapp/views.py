from django.shortcuts import render

# Create your views here.
def temp1(request):
    
    return render(request, "temp_in.html")

def temp2(request):
    
    return render(request, "temp_in2.html")
