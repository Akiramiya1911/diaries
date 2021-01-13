from django.db import models
from django.urls import reverse_lazy


class Classrooms(models.Model):

    teacher_name = models.CharField(max_length=150, null=True)
    classname = models.CharField(max_length=150)
    members = models.PositiveIntegerField()

    class Meta:
        db_table = 'classrooms'

    def get_absolute_url(self):
        return reverse_lazy('accounts:students_regist')
