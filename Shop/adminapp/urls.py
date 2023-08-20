from django.urls import path

from adminapp.views import admin_main, admin_user_read, admin_user_create, admin_user_update_delete, admin_book_read, \
    admin_book_create, admin_book_update, admin_book_delete, admin_author_read, admin_author_create, \
    admin_author_update, admin_author_delete

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
]
