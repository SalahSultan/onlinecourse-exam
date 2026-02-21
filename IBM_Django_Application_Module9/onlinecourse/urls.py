from django.urls import path
from . import views

app_name = 'onlinecourse'

urlpatterns = [
    # URL to submit an exam for a lesson
    path('lesson/<int:lesson_id>/submit/', views.submit, name='submit'),

    # URL to show the exam result for a submission
    path('submission/<int:submission_id>/result/', views.show_exam_result, name='show_exam_result'),
]