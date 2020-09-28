
from django.urls import path
from myapp import views
from django.views.generic.base import TemplateView

urlpatterns = [
    path('model/', views.model),
    
#    path('list/', views.list, name="list"), # FBV
    path('list/', views.ProductList.as_view(), name="list"), #CBV
    
#    path('write/', views.write, name="write_xxx"), # FBV
    path('write/', views.WriteCBV.as_view(), name="write_product"), # CBV
    # 비즈니스 로직 처리없이 화면만 보고 싶을 때(views를 안 거친다)
    path('writeForm/', TemplateView.as_view(template_name="writeForm.html"), name="writeForm_product"), #CBV
    
#    path('detail/<str:code>', views.detail, name="detail_product"), # FBV
    path('detail/<str:pk>', views.DetailCBV.as_view(), name="detail_product"), # CBV
    
    path('delete/', views.delete, name="delete_product"),
    path('update/', views.update, name="update_product"),
]
