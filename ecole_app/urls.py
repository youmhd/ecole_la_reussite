from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),


    path('students_list/', views.students_list, name='students-list'),
    path('add_student', views.add_student, name='add-student'),
    path('update_student/<student_id>', views.update_student, name='update-student'),
    path('delete_student/<student_id>', views.delete_student, name='delete-student'),
    path('show_student/<student_id>', views.show_student, name='show-student'),
    path('search_student', views.search_student, name='search-student'),

]    