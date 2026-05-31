 
from django.urls import path 
from .import views

urlpatterns = [
     
    path('',views.All_Card, name= ' All_Card' ),
    path("<int:stu_id>/", views.Card_Info, name="cardInfo")
]