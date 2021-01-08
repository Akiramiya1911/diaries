from django.db import models
from django.urls import reverse_lazy


class Classrooms(models.Model):

    classname = models.CharField(max_length=150)
    members = models.PositiveIntegerField()
    teacher = models.ForeignKey(
        'accounts.Teachers', on_delete=models.CASCADE
    )

    class Meta:
        db_table = 'classrooms'

    def get_absolute_url(self):
        return reverse_lazy('diary:home')
