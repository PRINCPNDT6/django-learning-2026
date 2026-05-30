 
from django.urls import path
from .import views 

urlpatterns = [
     
    path('',views.Login_System, name = 'Login_System'),
    path('<int:login_id>/', views.login_details, name='login_details')
    

]
