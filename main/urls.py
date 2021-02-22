from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('post/<int:post_id>/', views.detail, name='detail'),
    path('post/<int:post_id>/comment', views.leave_comment, name='comment')
]