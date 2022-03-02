from django.urls import path
from . import views

urlpatterns = [
    path('', views.login, name="login"),
    path('home', views.home, name="home"),
    path('sign',views.sign,name="sign"),
    path('details',views.details,name="details"),
    path('cart',views.cart,name="cart"),
     path('profile',views.profile,name="profile"),
    
]
