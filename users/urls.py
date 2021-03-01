from django.urls import path
from . import views

urlpatterns = [
    path('', views.profile, name='profile'),
    path('profile/<str:u_name>/', views.otherProfile, name='otherprofile'),
    path('follow_unfollow/', views.follow_unfollow, name='follow_unfollow'),
    path('register/', views.register, name='register'),
    path('login/', views.logIn, name='login'),
    path('logout/', views.logOut, name='logout'),
]
