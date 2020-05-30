from django import forms
from main import models

class ArticleForm(forms.ModelForm):
    class Meta:
        model = models.Article
        fields = ["title","body"]
