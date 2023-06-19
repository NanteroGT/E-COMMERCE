from django.urls import path
from shop.views import index, detail,checkout,contact,confirmation

urlpatterns=[
    path('',index,name='home'),
    path('<int:myid>',detail, name="detail"),
    path('checkout',checkout, name="checkout"),
    path('contact',contact,name="contact"),
    path('confirmation',confirmation,name="confirmation"),

]
