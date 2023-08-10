from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class  Post(models.Model):
    Title = models.CharField(max_length=23)
    Text= models.CharField
    Author=  models.ForeignKey(User, on_delete= models.CASCADE,related_name='blog_posts')
    Created_date= models.DateTimeField()
    Published_date= models.DateTimeField()

 
    def __str__(Self) -> str:
        return Self.name
