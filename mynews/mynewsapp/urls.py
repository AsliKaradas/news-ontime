from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from .views import NewsDetail

urlpatterns =  [
    path('home/', views.home, name='home'),
    path('', views.NewsList.as_view(), name="home"),
    path('add_news_post/', views.AddNewsPost.as_view(), name="add_news_post"),
    path('login_user/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout_user/', views.logout_user, name='logout'),
    path('signup_user/', views.signup_user, name='signup'),
    path('password_change/', auth_views.PasswordChangeView.as_view(), name='password_change'),
    path('password_change/done/', auth_views.PasswordChangeDoneView.as_view(), name='password_change_done'),
    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    path('news/<slug:slug>', views.NewsDetail.as_view(), name='article'),
    path('news/edit/<slug:slug>', views.UpdateNews.as_view(), name='edit'),
    path('news/delete/<slug:slug>', views.DeleteNews.as_view(), name='delete'),
    path('like/<slug:slug>', views.Like.as_view(), name='news_like'),
 ]