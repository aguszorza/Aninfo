from django.urls import path

from . import views

app_name = 'psatimetracker'

urlpatterns = [
    path('', views.index, name='index'),
    path('completeTask/', views.completeTask, name='completeTask'),
    path('completedTask/', views.taskCompleted, name='taskCompleted'),
]