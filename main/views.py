from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from main import models
from main import forms
from django.contrib.auth.decorators import login_required


def index(request):
    context = {
        'models' : models.Article.objects.all()
    }
    return render(request,'index.html',context = context)

def specificArticleAuthor(request,name):
    author = models.Author.objects.get(name = name)
    print(author)
    article = author.article_set.all()
    context = {
        'models' : article
    }
    return render(request,'nameArticle.html',context = context)


@login_required(login_url="auth/login")
def specificArticle(request):
    author = models.Author.objects.get(name = request.user)
    print(author)
    article = author.article_set.all()
    context = {
        'models' : article
    }
    return render(request,'nameArticle.html',context = context)


@login_required(login_url="auth/login")
def addArticle(request):
    error = None
    articleForm = forms.ArticleForm()

    if(request.method == "POST"):
        article = forms.ArticleForm(request.POST)
        author = None
        if(article.is_valid()):
            try:
                author = models.Author.objects.get(name = request.user)
            except:
                author = models.Author.objects.create(name = request.user)

            articleCreated = models.Article.objects.create(title = article.cleaned_data['title'],body = article.cleaned_data['body'],author = author)
            return HttpResponseRedirect('article')
        else:
            error = "Please fill the required details"

    context = {
        'forms' : articleForm,
        'error' : error
    }
    return render(request,'addArticle.html',context = context)
