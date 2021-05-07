from django.urls import path
from . import views


urlpatterns = [
    path('', views.apiOverview, name='api-overview'),
    path('posts/', views.postsList, name='posts-list'),
    path('posts/<int:id>/', views.postDetail, name='post-detail'),
]
