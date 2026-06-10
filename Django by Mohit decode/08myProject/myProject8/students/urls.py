 
from django.urls import path 
from students import views

urlpatterns = [
 path('', views.stu_Data, name='stu_data'),
 path('details/<int:student_id>/', views.stu_details, name='stu_details'),
 path('reviews/<int:review_id>/', views.stu_reviews, name='stu_review'),
 path('feedback/<int:feedback_id>/', views.stu_feedback, name='stu_feedback'),
 path('viewSelected/', views.stu_selected, name='stu_selected'),


]
