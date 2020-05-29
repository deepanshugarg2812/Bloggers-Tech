from django.db import models

# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length = 200)
    
    def __str__(self):
        return self.name

class Article(models.Model):
    title = models.CharField(max_length = 100,null=False,blank=False,default="")
    body = models.CharField(max_length = 2000)
    author = models.ForeignKey('Author',on_delete=models.CASCADE)

    def __str__(self):
        return self.title