from django.contrib import admin
from mainapp.models import BookCategory, Book, News, Comment


admin.site.register(BookCategory)
admin.site.register(Book)
admin.site.register(News)
admin.site.register(Comment)

