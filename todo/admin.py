from django.contrib import admin
from todo.models import Task

# 新しいモデルを書く
admin.site.register(Task)
