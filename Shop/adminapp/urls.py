from django.urls import path

from adminapp.views import admin_main, admin_user_read, admin_user_create, admin_user_update_delete, admin_book_read, \
    admin_book_create, admin_book_update, admin_book_delete, admin_author_read, admin_author_create, \
    admin_author_update, admin_author_delete, admin_quote_read, admin_quote_create, \
    admin_quote_update, admin_quote_delete, admin_genre_read, admin_genre_create, admin_genre_update, \
    admin_genre_delete

app_name = 'adminapp'

urlpatterns = [
    path('', admin_main, name='admin_main'),
    path('user_read/', admin_user_read, name='admin_user_read'),
    path('user_create/', admin_user_create, name='admin_user_create'),
    path('user_update_delete/', admin_user_update_delete, name='admin_user_update_delete'),

    path('book_read/', admin_book_read, name='admin_book_read'),
    path('book_create/', admin_book_create, name='admin_book_create'),
    path('admin_book_update/<str:book_id>/', admin_book_update, name='admin_book_update'),
    path('admin_book_delete/<str:book_id>/', admin_book_delete, name='admin_book_delete'),

    path('author_read/', admin_author_read, name='admin_author_read'),
    path('author_create/', admin_author_create, name='admin_author_create'),
    path('admin_author_update/<int:author_id>/', admin_author_update, name='admin_author_update'),
    path('admin_author_delete/<int:author_id>/', admin_author_delete, name='admin_author_delete'),

    path('genre_read/', admin_genre_read, name='admin_genre_read'),
    path('genre_create/', admin_genre_create, name='admin_genre_create'),
    path('admin_genre_update/<int:genre_id>/', admin_genre_update, name='admin_genre_update'),
    path('admin_genre_delete/<int:genre_id>/', admin_genre_delete, name='admin_genre_delete'),

    path('quote_read/', admin_quote_read, name='admin_quote_read'),
    path('quote_create/', admin_quote_create, name='admin_quote_create'),
    path('admin_quote_update/<int:quote_id>/', admin_quote_update, name='admin_quote_update'),
    path('admin_quote_delete/<int:quote_id>/', admin_quote_delete, name='admin_quote_delete'),
]
