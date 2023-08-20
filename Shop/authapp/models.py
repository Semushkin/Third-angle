from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):

    # NOT_SELECTED = '------'
    #
    # GENDER = {
    #     (NOT_SELECTED, '------'),
    #     ('М', 'М'),
    #     ('Ж', 'Ж')
    # }
    #
    # DEFAULT = '------'
    #
    # GROUP_USER = {
    #     (DEFAULT, 'Customer'),
    #     ('Seller', 'Seller'),
    #     ('Moderator', 'Moderator')
    # }
    #
    # gender = models.CharField(max_length=20, choices=GENDER, default=NOT_SELECTED)
    # in_group = models.CharField(max_length=20, choices=GROUP_USER, default=DEFAULT)
    # age = models.PositiveIntegerField(default=0)
    # address = models.CharField(max_length=100)
    # telephone = models.CharField(max_length=30)
    # date_update = models.DateField(auto_now_add=True)
    guid = models.CharField(max_length=128, blank=True, null=True)

    def __str__(self):
        return f'{self.username} {self.username}'
