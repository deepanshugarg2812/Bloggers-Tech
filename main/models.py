from django.db import models
from django.core.validators import (
    MinLengthValidator,
    MaxLengthValidator
)
 
# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length = 200)
    
    def __str__(self):
        return self.name

class Article(models.Model):
    title = models.CharField(max_length = 100,null=False,blank=False,default="",validators=[MinLengthValidator(10),MaxLengthValidator(100)])
    body = models.CharField(max_length = 2000,validators=[MinLengthValidator(500)])
    author = models.ForeignKey('Author',on_delete=models.CASCADE)

    def __str__(self):
        return self.title