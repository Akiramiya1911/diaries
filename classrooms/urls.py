from django.urls import path
from .views import (
    MakeClassroomView
)

app_name = 'classrooms'

urlpatterns = [
    path('make_classroom/', MakeClassroomView.as_view(), name='make_classroom'),
]
