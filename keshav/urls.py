from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import PasswordChangeView


urlpatterns = [
    path('', views.tweet_list, name='tweet_list'),
    path('create/', views.tweet_create, name='tweet_create'),
    path('tweet/<int:tweet_id>/edit/', views.tweet_edit, name='tweet_edit'),
    path('tweet/<int:tweet_id>/delete/', views.tweet_delete, name='tweet_delete'),
    # login and profile related urls
    path('login/', views.login, name='login'),
    path('register/', views.SignUp_view, name='register'),
    path('password/',views.custom_change_password, name='keshav'),
    path('done/',views.done, name='done'),
    path('userprofile/',views.profile_view, name='user_profile'),
    path('userprofile/update',views.profile_edit, name='update_profile'),
    # Blog one.
    path('keshav', views.keshav_list, name='keshav_list'),
    path('keshav/<int:pk>/', views.keshav_detail, name='keshav_detail'),
    path('keshav/new/', views.keshav_create, name='keshav_create'),
    path('keshav/<int:pk>/edit/', views.keshav_edit, name='keshav_edit'),
    path('keshav/<int:pk>/delete/', views.keshav_delete, name='keshav_delete'),
    path('accounts/', include('django.contrib.auth.urls')),

]