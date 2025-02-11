from django.urls import path
from . import views
from .views import signup, CustomLoginView, CustomLogoutView

urlpatterns = [
    path('', views.home, name='landingpage'),
    path('auction/', views.auction, name='auction'),
    path('forsale/', views.forsale, name='forsale'),
    path('addlisting/', views.addlisting, name='addlisting'),
    path('signup/', signup, name='signup'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', CustomLogoutView.as_view(), name='logout'),
]
