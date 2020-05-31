from django import forms
from django.core.validators import MinLengthValidator,MaxValueValidator,EmailValidator

class LoginForm(forms.Form):
    username = forms.CharField(validators=[MinLengthValidator(5)])
    password = forms.CharField(validators=[MinLengthValidator(5)])


class RegisterForm(forms.Form):
    first_name = forms.CharField(validators=[MinLengthValidator(5)])
    email = forms.EmailField(validators=[EmailValidator("Please enter the correct email")])
    username = forms.CharField(validators=[MinLengthValidator(5)])
    password = forms.CharField(validators=[MinLengthValidator(5)])
