from django.urls import path
from authentication import views

urlpatterns = ([
    path('/login',views.loginIndex),
    path('/register',views.registerIndex),
    path('/logout',views.logoutIndex),
])