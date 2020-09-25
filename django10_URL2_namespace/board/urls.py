
from django.urls import path
from django.urls.conf import include
from board import views

app_name = "board"
urlpatterns = [
    path('mainB/', views.mainB),
    
    path('boardAdd/', views.boardAdd, name="addData"),
    path('boardDel/', views.boardDel, name="delData"),
]
