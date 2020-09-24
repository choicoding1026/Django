
# myapp의 urls.py

from django.contrib import admin
from django.urls import path
from myapp import views

# http://localhost:8000/board/delete  ===> 삭제작업 ( views.py 에서 함수 구현)
# http://localhost:8000/board/update
# http://localhost:8000/board/select

urlpatterns = [
    path('delete/', views.delBoard ), # views.py에 가서 delBoard 함수호출
    path('update/', views.updateBoard ), # views.py에 가서 updateBoard 함수호출
    path('select/', views.selectBoard ), # views.py에 가서 updateBoard 함수호출
]









