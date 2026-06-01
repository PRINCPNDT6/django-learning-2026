 
from django.urls import path
from .import views 

urlpatterns = [
     
    path('',views.Login_System, name = 'Login_System'),
    path('details/vbit<int:login_id>/', views.login_details, name='login_details'),
    path('book/<int:book_id>/', views.book_Order, name='book_Order')
    

]
