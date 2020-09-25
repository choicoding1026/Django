
from django.urls import path
from myapp import views

urlpatterns = [
    
    path('link', views.link),
    
    path('main/memberInsert', views.memberInsert, name='insertData'),
    path('main/memberDelete', views.memberDelete, name='deleteData'),
    
]
