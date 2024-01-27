from django.urls import path
from todo.views import TaskListVies

urlpatterns = [
    path('', TaskListVies.as_view(), name='task-list')
]

