from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic.edit import CreateView
from .forms import TeacherLoginForm, TeacherRegistForm
from django.contrib.auth import login, authenticate


class TeacherLoginView(LoginView):

    template_name = 'teacher_login.html'
    authentication_form = TeacherLoginForm


class TeacherLogoutView(LogoutView):
    pass


class TeacherRegistView(CreateView):
    template_name = 'teacher_regist.html'
    form_class = TeacherRegistForm

    def form_valid(self, form):
        response = super().form_valid(form)
        username = form.cleaned_data.get('email')
        password = form.cleaned_data.get('password')
        teacher = authenticate(username=username, password=password)
        login(self.request, teacher)
        return response
