from django.urls import path
from . import views

urlpatterns = [
    path('', views.profile, name='profile'),
    path('<int:u_id>/', views.otherProfile, name='otherprofile'),
    path('register/', views.register, name='register'),
    path('login/', views.logIn, name='login'),
    path('logout/', views.logOut, name='logout'),
]
