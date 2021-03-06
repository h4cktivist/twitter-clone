from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('following/', views.following_users_posts, name='ollowing_users_posts'),
    path('post/<int:post_id>/', views.detail, name='detail'),
    path('post/<int:post_id>/comment', views.leave_comment, name='comment'),
    path('like/', views.like_post, name='like_post')
]
