from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='landingpage'),
    path('auction/', views.auction, name='auction'),
    path('forsale/', views.forsale, name='forsale'),
]
