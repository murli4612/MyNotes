from django.db import models

# Create your models here.
# class User(models.Model):
#     name = models.CharField(max_length = 15 )
#     username = models.CharField(max_length=15)
#     email = models.CharField(max_length=25)
    
#     def __str__(self):
#         return self.name

# class Post(models.Model):
#     user_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name='Post')
#     title = models.CharField(max_length=30)
#     body = models.TextField(max_length=200)

class Employee(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    
    
    
