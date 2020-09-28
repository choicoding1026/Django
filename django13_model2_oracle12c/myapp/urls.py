
from django.urls import path
from myapp import views

urlpatterns = [
    path('model/', views.model),
    path('list/', views.list, name="list"),
    path('write/', views.write, name="write_xxx"),
    path('writeForm/', views.writeForm, name="writeForm_product"),
    path('detail/<str:code>', views.detail, name="detail_product"),
    path('delete/', views.delete, name="delete_product"),
    path('update/', views.update, name="update_product"),
]
