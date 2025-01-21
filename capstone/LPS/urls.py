from django.urls import path
from . import views

urlpatterns = [
    path('', views.landingpage, name='landingpage'),
    path('profile/', views.profilepage, name='profilepage'),
    path('checkout/', views.checkoutpage, name='checkoutpage'),
    path('search/', views.searchingpage, name='searchingpage'),
]