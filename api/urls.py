from django.urls import path
from . import views


urlpatterns = [
    path('', views.apiOverview, name='api-overview'),
    path('posts-list/', views.postsList, name='posts-list'),
    path('post-detail/<int:id>', views.postDetail, name='post-detail'),
]
