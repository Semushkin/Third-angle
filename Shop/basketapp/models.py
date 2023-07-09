from django.db import models
from authapp.models import User
from mainapp.models import Book


DEFAULT_STATUS = 'Ожидает'

STATUS = {
    (DEFAULT_STATUS, DEFAULT_STATUS),
    ('В обработке', 'В обработке'),
    ('Готов к отгрузке', 'Готов к отгрузке'),
    ('Закрыт', 'Закрыт')
}


class Basket(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    create_date = models.DateField(auto_now_add=True)
    update_date = models.DateField(auto_now=True)
    status = models.CharField(max_length=20, choices=STATUS, default=DEFAULT_STATUS)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f'Карзина пользователя {self.user}'


class Request(models.Model):

    text = models.TextField()
    create_date = models.DateField(auto_now_add=True)
    update_date = models.DateField(auto_now=True)
    status = models.CharField(max_length=20, choices=STATUS, default=DEFAULT_STATUS)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'Запрос пользователя {self.user}'
