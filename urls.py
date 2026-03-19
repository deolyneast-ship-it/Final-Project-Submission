from django.urls import path
from . import views

app_name = 'onlinecourse'
urlpatterns = [
    # ... other paths for index, course details, etc.
    
    # Path for Task 6
    path('course/<int:course_id>/submission/', views.submit, name='submit'),
    path('course/<int:course_id>/submission/<int:submission_id>/result/', views.show_exam_result, name='show_exam_result'),
]
