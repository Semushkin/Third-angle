from django.shortcuts import render
from mainapp.models import Book
from authapp.forms import UserRegisterForm, UserLoginForm, UserEditForm, SetNewPassword
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from mainapp.forms import BoorCreateUpdateForm


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
    if request.method == 'POST':
        form = BoorCreateUpdateForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            # print(f'id ========= {form.instance.id}')
            return HttpResponseRedirect(reverse('m_product_detail', args=[form.instance.id]))
    else:
        form = BoorCreateUpdateForm()
    context = {
        'form': form,
    }
    return render(request, 'sellerapp/product_create.html', context)


def product_edit(request, book_id):
    book = Book.objects.get(pk=book_id)
    if request.method == 'POST':
        form = BoorCreateUpdateForm(instance=book, data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('m_product_detail', args=[form.instance.id]))
        else:
            pass
    else:
        form = BoorCreateUpdateForm(instance=book)
    context = {
        'form': form,
        'book': book,
    }
    return render(request, 'sellerapp/product_edit.html', context)


def product_delete(request, book_id):
    book = Book.objects.get(pk=book_id)
    book.delete()
    return HttpResponseRedirect(reverse('products_list'))


def m_quote_detail(request):
    return render(request, 'sellerapp/m_quote_detail.html')


def m_new_detail(request):
    return render(request, 'sellerapp/m_new_detail.html')


def m_product_detail(request, book_id):
    context = {
        'book': Book.objects.get(pk=book_id)
    }
    return render(request, 'sellerapp/m_product_detail.html', context)


def order_list(request):
    return render(request, 'sellerapp/order_list.html')