from django.urls import path
from . import views

app_name = 'tasks'

urlpatterns = [
    path('tasks/', views.tasks),
    path('tasks/<int:pk>', views.task_detail),
    path('tasklist/', views.TaskListView.as_view()),
    path('preset/', views.PresetView.as_view()),
]
