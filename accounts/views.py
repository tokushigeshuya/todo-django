from django.views.generic import CreateView
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy

# Create your views here.

class MyLoginView(LoginView):
  template_name = 'accounts/login.html'
  # falseだとログイン後もログイン画面に戻ってくる trueで他のURL設定が可能
  # false → login/ → login/
  # true → login/ → 　task-list/
  redirect_autheticated_user = True

class SignUpView(CreateView):
  form_class = UserCreationForm
  template_name = 'accounts/signup.html'
  success_url = reverse_lazy('task-list')