from django.urls import path
from main import views

urlpatterns = [
    path('',views.index,name = "articles"),
    path('article/<str:name>',views.specificArticle,name = "article"),
]