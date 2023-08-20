from django.db import models
from authapp.models import User


class BookCategory(models.Model):
    name = models.CharField(max_length=64, unique=True)

    def __str__(self):
        return f'{self.name}'


class Book(models.Model):
    name = models.CharField(max_length=64)
    author = models.CharField(max_length=64, blank=True)
    foto = models.ImageField(upload_to='book_images', blank=True)
    article = models.IntegerField()
    date_receipt = models.DateField()
    category = models.ForeignKey(BookCategory, on_delete=models.CASCADE)
    description = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    date_create = models.DateField(auto_now_add=True)
    date_update = models.DateField(auto_now=True)

    def __str__(self):
        return f'{self.name}'


class ImageBook(models.Model):
    guid = models.CharField(max_length=128)
    foto = models.ImageField(upload_to='book_images', blank=True)

    def __str__(self):
        return f'Images for {self.guid}'


class News(models.Model):
    name = models.CharField(max_length=128, default='')
    description = models.TextField()
    text = models.TextField()
    foto = models.ImageField(upload_to='news_images', blank=True)
    date_create = models.DateField(auto_now_add=True)
    date_update = models.DateField(auto_now=True)

    def __str__(self):
        return f'{self.text[0:20]}'


class Quote(models.Model):
    name = models.CharField(max_length=64)
    text = models.TextField()
    author = models.CharField(max_length=64)
    is_active = models.BooleanField(default=False)
    date_create = models.DateField(auto_now_add=True)
    date_update = models.DateField(auto_now=True)

    def __str__(self):
        return f'Цитата: {self.name}'


class Comment(models.Model):
    STARS = ((5, "⭐⭐⭐⭐⭐"), (4, "⭐⭐⭐⭐"), (3, "⭐⭐⭐"), (2, "⭐⭐"), (1, "⭐"))

    text = models.TextField()
    starts = models.SmallIntegerField(choices=STARS, default='1')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    date_create = models.DateField(auto_now_add=True)
    date_update = models.DateField(auto_now=True)

    def __str__(self):
        return f'Отзыв по книге: "{self.book}", пользователь: {self.user}'


class Authors(models.Model):
    person = models.CharField(max_length=128, unique=True)

    def __str__(self):
        return self.person