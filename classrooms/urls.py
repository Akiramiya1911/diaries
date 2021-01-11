from django.urls import path
from .views import (
    MakeClassroomView, SelectClassRoomView
)

app_name = 'classrooms'

urlpatterns = [
    path('select_classroom', SelectClassRoomView.as_view(), name='select_classroom'),
    path('make_classroom/', MakeClassroomView.as_view(), name='make_classroom'),
]
