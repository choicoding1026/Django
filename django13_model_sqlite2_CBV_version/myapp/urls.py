
from django.urls import path
from myapp import views
from django.views.generic.base import TemplateView

urlpatterns = [
    path('model/', views.model),
    
#     path('list/', views.list, name="list"),
    path('list/', views.ProductListCBV.as_view(), name="list"),

#     path('write/', views.write, name="write_xxx"),
    path('write/', views.ProductWriteCBV.as_view(), name="write_product"),
    
#     path('writeForm/', views.writeForm, name="writeForm_product"),
    path('writeForm/', TemplateView.as_view(template_name="writeForm.html"), name="writeForm_product"),

#     path('detail/<str:code>', views.detail, name="detail_product"),
    path('detail/<str:pk', views.ProductDetailCBV.as_view(), name="detail_product"),
    
#     path('delete/', views.delete, name="delete_product"),
    path('delte/', views.ProductDeleteCBV.as_view(), name="delete_product"),
    
#     path('update/', views.update, name="update_product"),
    path('update/', views.ProductUpdateCBV.as_view(), name="update_product"),
]
