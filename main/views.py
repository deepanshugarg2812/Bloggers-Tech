from django.shortcuts import render
from django.http import HttpResponse
from main import models

# Create your views here.
def index(request):
    context = {
        'models' : models.Article.objects.all()
    }
    return render(request,'index.html',context = context)

def specificArticle(request,name):
    author = models.Author.objects.get(name = name)
    article = author.article_set.all()
    context = {
        'models' : article
    }
    return render(request,'nameArticle.html',context = context)