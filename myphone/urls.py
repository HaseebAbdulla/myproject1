from django.urls import path
from . import views

urlpatterns = [
    path('', views.login, name="login"),
    path('home', views.home, name="home"),
    path('sign',views.sign,name="sign"),
    path('details',views.details,name="details"),
    path('cart',views.cart,name="cart"),
    path('profile',views.profile,name="profile"),
    path('dtls1',views.dtls1,name="dtls1"),
    path('dtls2',views.dtls2,name="dtls2"),
    path('dtls3',views.dtls3,name="dtls3"),
    path('logout',views.logout,name="logout")
    
]
