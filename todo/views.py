from django.shortcuts import render
from django.views.generic import ListView,DetailView,CreateView,DeleteView
from django.urls import reverse_lazy

from todo.models import Task
# Create your views here.
class TaskListVies(ListView):
  model = Task
  template_name = 'todo/task_list.html'

class TaskDetailView(DetailView):
  model = Task
  template_name = 'todo/task_detail.html'

class TaskCreateView(CreateView):
  model = Task
  fields = '__all__'
  success_url = reverse_lazy('task-list')
  template_name = 'todo/task_form.html'

class TaskDeleteView(DeleteView):
  model = Task
  success_url = reverse_lazy('task-list')
  template_name = 'todo/task_delete.html'