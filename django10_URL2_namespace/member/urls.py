
from django.urls import path
from django.urls.conf import include
from member import views

app_name = "member"
urlpatterns = [
    path('mainM/', views.mainM),
    
    path('memberAdd/', views.memberAdd, name="addData"),
    path('memberDel/', views.memberDel, name="delData"),
]