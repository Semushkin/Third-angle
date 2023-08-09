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


class Order(models.Model):
    create_date = models.DateField(auto_now_add=True)
    update_date = models.DateField(auto_now=True)
    status = models.CharField(max_length=20, choices=STATUS, default=DEFAULT_STATUS)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def sum(self):
        baskets = Basket.objects.filter(order=self.pk)
        return sum(basket.sum() for basket in baskets)


class Basket(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    order = models.ForeignKey(Order, on_delete=models.CASCADE, null=True, blank=True)
    create_date = models.DateField(auto_now_add=True)
    update_date = models.DateField(auto_now=True)
    # status = models.CharField(max_length=20, choices=STATUS, default=DEFAULT_STATUS)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f'Карзина пользователя {self.user}'

    def sum(self):
        return self.quantity * self.book.price

    def get_basket(self):
        return Basket.objects.filter(user=self.user, order=None)

    def total_sum(self):
        baskets = self.get_basket()
        return sum(basket.sum() for basket in baskets)


class Request(models.Model):

    text = models.TextField()
    create_date = models.DateField(auto_now_add=True)
    update_date = models.DateField(auto_now=True)
    status = models.CharField(max_length=20, choices=STATUS, default=DEFAULT_STATUS)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.text[0:20]}'
