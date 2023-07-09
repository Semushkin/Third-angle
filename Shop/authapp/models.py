from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):

    NOT_SELECTED = '------'

    GENDER = {
        (NOT_SELECTED, '------'),
        ('М', 'М'),
        ('Ж', 'Ж')
    }

    gender = models.CharField(max_length=20, choices=GENDER, default=NOT_SELECTED)
    age = models.PositiveIntegerField(default=0)
    address = models.CharField(max_length=100)
    telephone = models.CharField(max_length=16)
    date_update = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'{self.username} {self.username}'
