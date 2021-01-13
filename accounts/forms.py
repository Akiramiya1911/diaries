from django import forms
from .models import Students
from classrooms.models import Classrooms
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError


class StudentsRegistForm(forms.ModelForm):
    attendance_number = forms.CharField(label='出席番号')
    username = forms.CharField(label='氏名')
    password = forms.CharField(label='初期パスワード', widget=forms.PasswordInput())
    confirm_password = forms.CharField(label='初期パスワード(確認用)', widget=forms.PasswordInput())

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
        classroom = Classrooms.objects.last()
        student.classroom_id = classroom.id
        student.save()
        return student
