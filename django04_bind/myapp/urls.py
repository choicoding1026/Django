
from django.contrib import admin
from django.urls import path
from myapp import views

urlpatterns = [
    path('a/', views.template_a ),
    path('b/', views.template_b ),
    path('c/', views.template_c ),
    path('d/', views.template_d ),
    path('e/', views.template_e ),
    path('f/', views.template_f ),
    path('g/', views.template_g ),
]
