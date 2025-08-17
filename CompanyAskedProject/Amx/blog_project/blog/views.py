from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from .models import Post

from .serializers import PostSerializers

class PostListCreateView(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializers
    
    def perform_create(self, serializer):
        serializer.save()

class PostDetailsView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializers