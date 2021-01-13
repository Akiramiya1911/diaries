from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    path('students_regist/', views.student_regist_view, name="students_regist"),
]
