from django.urls import path
from .views import registeruser,loginuser,Sellerproductlist,orderlist

urlpatterns = [
    path('register/',registeruser,name='registercustomer'),
    path('login/',loginuser,name='logincustomer'),
    path('sellerprod/<str:username>/',Sellerproductlist,name='seller products'),
    path('orderlist/<str:username>/',orderlist,name='ordered products'),
    
    
    
    
]
