from django.urls import path

from .views import PostListCreateView, PostDetailsView

urlpatterns = [
    path('posts/', PostListCreateView.as_view(), name = 'post-list'),
    path('posts/<int:pk>/',PostDetailsView.as_view(),name = 'post-detils')
]