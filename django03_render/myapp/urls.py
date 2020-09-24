
from django.contrib import admin
from django.urls import path
from myapp import views

# myapp의 urls.py

# http://localhost:8000/first/req1
urlpatterns = [
    path('req1/', views.req1 ),
]
