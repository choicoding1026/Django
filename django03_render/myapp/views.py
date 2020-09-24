from django.shortcuts import render

# Create your views here.
def req1(request):
    
#     return render(request, "first_template.html") # myapp의 templates 폴더에 찾는다.
    return render(request, "polls/second_template.html") # myapp의 templates 폴더에 찾는다.