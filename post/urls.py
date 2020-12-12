from django.contrib import admin
from django.urls import path , include

from . import views
app_name='post'
urlpatterns = [
   path('', views.PoostList.as_view()),
    path('<int:pk>/' , views.PoostDetail.as_view()),
    ]