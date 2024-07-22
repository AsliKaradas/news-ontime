from django.urls import path
from . import views

urlpatterns =  [
    path('', views.NewsList.as_view(), name="home"),
    path('add_news/', views.AddNewsPost.as_view(), name="add_news"),
 ]