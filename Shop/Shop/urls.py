from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from mainapp.views import *
from authapp.views import *
from basketapp.views import *
from sellerapp.views import *
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('catalog/', catalog, name='catalog'),
    path('search_result/', search_result, name='search_result'),
    path('news/', news, name='news'),
    path('contacts/', contacts, name='contacts'),
    path('about/', about, name='about'),
    path('cart/', cart, name='cart'),
    path('edit_profile/', edit_profile, name='edit_profile'),
    path('login/', login, name='login'),
    path('logout/', logout, name='logout'),
    path('order_detail/<int:order_id>/', order_detail, name='order_detail'),
    path('order_list/', order_list, name='order_list'),
    path('profile/', profile, name='profile'),
    path('registration/', registration, name='registration'),
    path('rules/', rules, name='rules'),
    path('s_order_detail/<int:order_id>/', s_order_detail, name='s_order_detail'),
    path('s_search_detail/', s_search_detail, name='s_search_detail'),
    path('search_detail/', search_detail, name='search_detail'),
    path('search_list/', search_list, name='search_list'),
    path('new_detail/<int:new_id>/', new_detail, name='new_detail'),
    path('product_detail/<int:book_id>/', product_detail, name='product_detail'),
    path('m_profile/', m_profile, name='m_profile'),
    path('s_profile/', s_profile, name='s_profile'),
    path('news_list/', news_list, name='news_list'),
    path('new_create/', new_create, name='new_create'),
    path('new_edit/<int:news_id>/', new_edit, name='new_edit'),
    path('new_delete/<int:news_id>/', new_delete, name='new_delete'),
    path('quotes_list/', quotes_list, name='quotes_list'),
    path('quote_create/', quote_create, name='quote_create'),
    path('quote_edit/<int:quote_id>/', quote_edit, name='quote_edit'),
    path('quote_delete/<int:quote_id>/', quote_delete, name='quote_delete'),
    path('products_list/', products_list, name='products_list'),
    path('product_create/', product_create, name='product_create'),
    path('product_edit/<int:book_id>/', product_edit, name='product_edit'),
    path('product_delete/<int:book_id>/', product_delete, name='product_delete'),
    path('m_quote_detail/<int:quote_id>/', m_quote_detail, name='m_quote_detail'),
    path('m_new_detail/<int:news_id>/', m_new_detail, name='m_new_detail'),
    path('m_product_detail/<int:book_id>/', m_product_detail, name='m_product_detail'),

    path('basket/', include('basketapp.urls', namespace='basket')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
