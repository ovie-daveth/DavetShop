from django.urls import path
from . import views

app_name='item'
urlpatterns = [
     path('', views.create, name='create'),
    path('detail/<str:pk>/', views.detail, name='detail')
]