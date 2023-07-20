from django.shortcuts import render
from mainapp.models import Book
from authapp.forms import UserRegisterForm, UserLoginForm, UserEditForm, SetNewPassword
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator


def s_order_detail(request):
    return render(request, 'sellerapp/s_order_detail.html')


def s_search_detail(request):
    return render(request, 'sellerapp/s_search_detail.html')


def search_list(request):
    return render(request, 'sellerapp/search_list.html')


def new_detail(request):
    return render(request, 'sellerapp/new_detail.html')


def product_detail(request):
    return render(request, 'sellerapp/product_detail.html')


def m_profile(request):
    return render(request, 'sellerapp/m_profile.html')


def s_profile(request):
    return render(request, 'sellerapp/s_profile.html')


def news_list(request):
    return render(request, 'sellerapp/news_list.html')


def new_create(request):
    return render(request, 'sellerapp/new_create.html')


def new_edit(request):
    return render(request, 'sellerapp/new_edit.html')


def quotes_list(request):
    return render(request, 'sellerapp/quotes_list.html')


def quote_create(request):
    return render(request, 'sellerapp/quote_create.html')


def quote_edit(request):
    return render(request, 'sellerapp/quote_edit.html')


def products_list(request):
    context = {
        'books': Book.objects.all(),
    }
    return render(request, 'sellerapp/products_list.html', context)


def product_create(request):
    return render(request, 'sellerapp/product_create.html')


def product_edit(request):
    return render(request, 'sellerapp/product_edit.html')


def m_quote_detail(request):
    return render(request, 'sellerapp/m_quote_detail.html')


def m_new_detail(request):
    return render(request, 'sellerapp/m_new_detail.html')


def m_product_detail(request):
    return render(request, 'sellerapp/m_product_detail.html')


def order_list(request):
    return render(request, 'sellerapp/order_list.html')