from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from main import models
from main import forms

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

def addArticle(request):
    error = None
    articleForm = forms.ArticleForm()

    if(request.method == "POST"):
        article = forms.ArticleForm(request.POST)
        print(article)
        if(article.is_valid()):
            return HttpResponse("Good")
        else:
            error = "Please fill the required details"

    context = {
        'forms' : articleForm,
        'error' : error
    }
    return render(request,'addArticle.html',context = context)
