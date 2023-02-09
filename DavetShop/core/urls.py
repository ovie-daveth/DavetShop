from django.urls import path
from . import views
from .forms import LoginForm
from django.contrib.auth import views as auth_view

app_name = 'core'
urlpatterns = [
    path('', views.index, name="index"),
    path('register', views.register, name="register"),
    path('login', auth_view.LoginView.as_view(template_name='core/login.html', authentication_form=LoginForm), name="login"),
    path('logout', views.signout, name="logout")
]