from django.contrib import admin
from django.urls import path
from mainapp.views import index, catalog, news, contacts, about

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('catalog/', catalog, name='catalog'),
    path('news/', news, name='news'),
    path('contacts/', contacts, name='contacts'),
    path('about/', about, name='about'),
]
