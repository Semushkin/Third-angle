from django.contrib import admin
from mainapp.models import BookCategory, Book, News, Comment, Authors



admin.site.register(BookCategory)
admin.site.register(Book)
admin.site.register(News)
admin.site.register(Comment)
admin.site.register(Authors)

