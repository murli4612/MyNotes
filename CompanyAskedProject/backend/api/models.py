from django.db import models

# Create your models here.

# Build a RESTful API that manages movies and their reviews.
# Implement endpoints to create, retrieve, update, and delete movies.
# Support the addition and removal of reviews for individual movies.
# Optionally integrate a SQL database for persistent storage.
# Ensure proper error handling, data validation, and appropriate HTTP status code
# class Movie(models.Model):
#     title  = models.CharField(max_length=30)
#     release_year = models.PositiveIntegerField()
#     created_at = models.DateTimeField(auto_now_add=True)
    
#     def __str__(self):
#         return self.title


from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from rest_framework import serializers, viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.routers import DefaultRouter
from django.urls import path, include
from django.shortcuts import get_object_or_404
from rest_framework.exceptions import ValidationError
# Models
class Movie(models.Model):
    title = models.CharField(max_length=255, unique=True)
    description = models.TextField()
    release_year = models.PositiveIntegerField()

    def __str__(self):
        return self.title

class Review(models.Model):
    movie = models.ForeignKey(Movie, related_name='reviews', on_delete=models.CASCADE)
    reviewer = models.CharField(max_length=100)
    rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(10)])
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.reviewer} - {self.movie.title}"