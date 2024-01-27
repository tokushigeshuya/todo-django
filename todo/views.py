from django.shortcuts import render
from django.views.generic import ListView

from todo.models import Task
# Create your views here.
class TaskListVies(ListView):
  model = Task
  template_name = 'todo/task_list.html'