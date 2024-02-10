from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('results/', views.results, name='results'),
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('create_details/', views.user_details_create_view, name='create_details'),
    path('create_activity/', views.user_activity_create_view, name='create_activity'),
    path('rendering/', views.rendering, name='rendering'),
    path('gain_calories/', views.gain_calories, name='gain_calories'),
    path('eat_up/', views.eat_up, name='eat_up'),
    path('breakfast/', views.breakfast, name='breakfast'),
]