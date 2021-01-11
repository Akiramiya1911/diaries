from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser, PermissionsMixin
)
from django.urls import reverse_lazy


class UserManager(BaseUserManager):

    def create_user(self, attendance_number, username, email, password=None):
        user = self.model(
            attendance_number=attendance_number,
            username=username,
            email=email
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, attendance_number, username, email, password=None):
        user = self.model(
            attendance_number=attendance_number,
            username=username,
            email=email,
        )
        user.set_password(password)
        user.is_staff = True
        user.is_active = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class Students(AbstractBaseUser, PermissionsMixin):

    attendance_number = models.PositiveIntegerField(unique=True)
    username = models.CharField(max_length=150)
    email = models.EmailField(max_length=255, null=True, blank=True)
    classroom = models.ForeignKey(
        'classrooms.Classrooms', on_delete=models.CASCADE
    )

    USERNAME_FIELD = 'attendance_number'
    REQUIRED_FIELDS = ['username', ]

    objects = UserManager()

    def get_absolute_url(self):
        return reverse_lazy('diary:home')

    class Meta:
        db_table = 'students'
