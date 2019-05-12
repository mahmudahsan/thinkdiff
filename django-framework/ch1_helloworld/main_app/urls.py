from django.urls import path 
from . import views

urlpatterns = [
    path('', views.homeView, name="home"),
    path('home/', views.homeView, name="home"),
    path('another/', views.anotherView, name="another")
]