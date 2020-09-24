"""django02_HttpResponse URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# project단위의 urls.py
# http://localhost:8000/project요청/app요청
# http://localhost:8000/aaa/bbb
# 
# http://localhost:8000//delete
# http://localhost:8000/board/update
# http://localhost:8000/board/select



from django.contrib import admin
from django.urls import path
from django.urls.conf import include
# project단위의 urls.py
urlpatterns = [
    path('admin/', admin.site.urls),
    path('board/', include('myapp.urls')), # myapp어플리케이션내의 urls.py 등록
]










