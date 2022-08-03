from django.urls import URLPattern, path
from .import views


urlpatterns=[
    path('adminmaster', views.adminmaster, name="adminmaster"),
]


