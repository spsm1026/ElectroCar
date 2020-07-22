from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login, name="login"),
    path('logout/', views.logout, name="logout"),
    path('register/', views.register, name="register"),    
    path('home/', views.home, name="home"),       
    path('find/', views.find, name="find"),    
    path('find_password/', views.find_password, name="find_password"),    
    path('new_password/', views.new_password, name="new_password"),    
]
