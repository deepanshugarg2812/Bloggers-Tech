from django.urls import path
from main import views

urlpatterns = [
    path('',views.index,name = "articles"),
    path('author/article/<str:name>',views.specificArticleAuthor),
    path('article/',views.specificArticle,name = "article"),
    path('addArticle',views.addArticle,name = "addArticle"),
]