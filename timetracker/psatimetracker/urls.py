from django.urls import path

from . import views

app_name = 'psatimetracker'

urlpatterns = [
    path('', views.index, name='index'),
    path('completeTaskHours/', views.completeTaskHours, name='completeTaskHours'),
    path('completedTaskHours/', views.taskHoursCompleted, name='completedTaskHours'),
]