from django.urls import path
from student import views

urlpatterns = [
    path('', views.Student_list, name = 'Student_list'),
    path('add/', views.student_create, name = 'student_create'),
    path('details/<int:detail_id>/', views.stu_details, name = 'stu_details'),
    path('edit/<int:edit_id>/', views.stu_edit, name = 'edit_stu'),
    path('del/<int:del_id>/', views.stu_delete, name = 'stu_del'),
]
