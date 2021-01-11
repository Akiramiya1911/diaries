from django.urls import path
from .views import (
    TeacherLoginView, TeacherLogoutView, TeacherRegistView
)

app_name = 'accounts'

urlpatterns = [
    path('teacher_login/', TeacherLoginView.as_view(), name="teacher_login"),
    path('teacher_logout/', TeacherLogoutView.as_view(), name="teacher_logout"),
    path('teacher_regist/', TeacherRegistView.as_view(), name="teacher_regist"),
]
