from django.db import models

# Create your models here.
class Author(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField(unique=True)
    bio=models.TextField(blank=True)

class Category(models.Model):
    name=models.CharField(max_length=50,unique=True)
    decription=models.TextField(black=true)

class Post(models.Model):
    title=models.CharFeild(max_length=200)
    content=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now_add=True)
    author=models.ForeignKey(Author,on_delete=models.CASCADE,related_name=posts)
    category=models.ForeignKey(Category,related_name=posts)