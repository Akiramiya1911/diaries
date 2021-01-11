from django import forms
from .models import Students
from django.contrib.auth.password_validation import validate_password
from django.contrib.auth.forms import AuthenticationForm
from django.core.exceptions import ValidationError


class TeacherLoginForm(AuthenticationForm):
    username = forms.EmailField(label='メールアドレス')
    password = forms.CharField(label='パスワード', widget=forms.PasswordInput())


class TeacherRegistForm(forms.ModelForm):
    attendance_number = forms.IntegerField(label='出席番号', min_value=1)
    username = forms.CharField(label='氏名')
    password = forms.CharField(label='パスワード', widget=forms.PasswordInput())
    confirm_password = forms.CharField(label='パスワード', widget=forms.PasswordInput())

    class Meta:
        model = Students
        fields = ['attendance_number', 'username', 'password']

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')
        if password != confirm_password:
            raise ValidationError('パスワードが一致しません')

    def save(self, commit=False):
        student = super().save(commit=False)
        validate_password(self.cleaned_data['password'], student)
        student.set_password(self.cleaned_data['password'])
        student.save()
        return student
