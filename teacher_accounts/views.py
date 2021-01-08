from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic.edit import CreateView
from .forms import TeacherLoginForm, TeacherRegistForm


class TeacherLoginView(LoginView):

    template_name = 'teacher_login.html'
    authentication_form = TeacherLoginForm


class TeacherLogoutView(LogoutView):
    pass


class TeacherRegistView(CreateView):
    template_name = 'teacher_regist.html'
    form_class = TeacherRegistForm
