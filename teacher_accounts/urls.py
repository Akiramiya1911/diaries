from django.urls import path
from .views import TeacherLoginView, TeacherLogoutView

app_name = 'teacher_accounts'

urlpatterns = [
    path('teacher_login/', TeacherLoginView.as_view(), name="teacher_login"),
    path('teacher_logout/', TeacherLogoutView.as_view(), name="teacher_logout"),
]
