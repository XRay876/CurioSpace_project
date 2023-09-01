
from django.urls import path, re_path, include
from django.contrib.auth import views
from . import views
from .views import UserLoginView, UserLogoutView

urlpatterns = [
    path('', views.profile, name='home'),
    # path('register/', views.RegisterUser.as_view(), name='register'),
    path('register/', views.register, name='register'),
    # path('login/', views.login, name='login'),
    path('login/', UserLoginView.as_view(), name='login'),
    # path('login/', include('django.contrib.auth.urls'), name='login'),
    path('logout/', UserLogoutView.as_view(), name='logout'),
       

    
]
