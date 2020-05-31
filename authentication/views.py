from django.shortcuts import render
from authentication import forms
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.contrib.auth import login,logout


def loginIndex(request):
    if request.user == "AnonymousUser":
        print(request.user)
        return HttpResponseRedirect('/addArticle')

    loginForm = forms.LoginForm()
    error = None

    if(request.method == 'POST'):
        loginData = forms.LoginForm(request.POST)
        if loginData.is_valid():
            username = loginData.cleaned_data['username']
            password = loginData.cleaned_data['password']
            user = authenticate(username = username,password = password)
            if user:
                login(request,user)
                return HttpResponseRedirect('/addArticle')
            else:
                error = "Please enter the valid email and password"
        else:
            error = "Please enter the detals properly"

    context = {
        'forms' : loginForm,
        'error' : error
    }

    return render(request,'auth/login.html',context)

def registerIndex(request):
    if request.user:
        return HttpResponseRedirect('/addArticle')

    RegisterForm = forms.RegisterForm()
    error = None

    if(request.method == 'POST'):
        registerData = forms.RegisterForm(request.POST)
        if registerData.is_valid():
            first_name = registerData.cleaned_data['first_name']
            email = registerData.cleaned_data['email']
            username = registerData.cleaned_data['username']
            password = registerData.cleaned_data['password']
            user= User.objects.get(username=username)
            if user:
                error = "User already exist"
            else:
                user = User.objects.create_user(username= username,password = password,email = email,first_name=first_name)
                if user:
                    login(request,user)
                    return HttpResponseRedirect('/auth/login')

        else:
            error = "Please enter the detals properly"

    context = {
        'forms' : RegisterForm,
        'error' : error
    }

    return render(request,'auth/register.html',context)

def logoutIndex(request):
    logout(request)
    return HttpResponseRedirect('/auth/login')