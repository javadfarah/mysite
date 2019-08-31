    
from django.contrib import admin
from django.urls import path,include
from project import views


urlpatterns = [
    path('', views.home, name='index'),
    path('detail/<int:id>', views.post_details, name='post_details'),
    path('posts/<str:kind>', views.post_list, name='post_list'),
    path('search/', views.search, name='search'),



]
    