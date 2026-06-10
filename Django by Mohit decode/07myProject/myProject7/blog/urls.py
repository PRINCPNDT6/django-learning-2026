 
from django.urls import path
from . import views

urlpatterns = [
    path('', views.blog_list, name='blog_list'),
    path('home/', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('profile/<int:user_id>/', views.profile, name='profile'),
    path('edit/<int:user_id>/', views.editUser, name='edit_user'),
    path('alluser/', views.alluserData, name='alluserData'),
     
]