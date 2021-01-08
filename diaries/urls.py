from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('diary/', include('diary.urls')),
    path('accounts/', include('accounts.urls')),
    path('classrooms/', include('classrooms.urls')),
]
