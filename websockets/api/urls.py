from django.urls import path
from . import views

urlpatterns = [
    path('', views.chat, name = "index"),
    path('index/', views.index, name = "index"),
]
