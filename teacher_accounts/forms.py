from django import forms
from .models import Teachers
from django.contrib.auth.password_validation import validate_password
from django.contrib.auth.forms import AuthenticationForm


class TeacherLoginForm(AuthenticationForm):
    username = forms.EmailField(label='メールアドレス')
    password = forms.CharField(label='パスワード', widget=forms.PasswordInput())


class TeacherRegistForm(forms.ModelForm):
    username = forms.CharField(label='氏名')
    email = forms.EmailField(label='メールアドレス')
    password = forms.CharField(label='パスワード', widget=forms.PasswordInput())

    class Meta:
        model = Teachers
        fields = ['username', 'email', 'password']

    def save(self, commit=False):
        teacher = super().save(commit=False)
        validate_password(self.cleaned_data['password'], teacher)
        teacher.set_password(self.cleaned_data['password'])
        teacher.save()
        return teacher
