from django.contrib.auth.views import LoginView

# Create your views here.

class MyLoginView(LoginView):
  template_name = 'accounts/login.html'
  # falseだとログイン後もログイン画面に戻ってくる trueで他のURL設定が可能
  # false → login/ → login/
  # true → login/ → 　task-list/
  redirect_autheticated_user = True