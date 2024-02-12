from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),

    path('create_details/', views.user_details_create_view, name='create_details'),
    path('results/', views.results, name='results'),
    path('rendering/', views.rendering, name='rendering'),
    path('consume_calory/', views.consume_calory, name='consume_calory'),
    path('burn_calory/', views.burn_calory, name='burn_calory'),
    path('fd/', views.food_list_on_date, name='fd'),
]