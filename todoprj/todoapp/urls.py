from django.urls import path
from django.contrib.auth.views import LogoutView
from . import views

urlpatterns = [
    path('', views.home, name='home-page'),
    path('logout/', views.logoutView, name='logout'),
    path('register/', views.register, name='register'),
    path('login/', views.loginPage, name='login'),
    path('delete-task/<str:name>/', views.DeleteTask, name='delete'),
    path('update/<str:name>/', views.Update, name='update'),
]
