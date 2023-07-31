from django.shortcuts import render
from mainapp.models import Book, News, Quote
from authapp.forms import UserRegisterForm, UserLoginForm, UserEditForm, SetNewPassword
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from mainapp.forms import BoorCreateUpdateForm, NewsCreateUpdateForm, QuoteCreateUpdateForm


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
    news = News.objects.all()
    context = {
        'news': news
    }
    return render(request, 'sellerapp/news_list.html', context)


def new_create(request):
    if request.method == 'POST':
        form = NewsCreateUpdateForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('m_new_detail', args=[form.instance.id]))
    else:
        form = NewsCreateUpdateForm()
    context = {
        'form': form,
    }
    return render(request, 'sellerapp/new_create.html', context)


def new_edit(request, news_id):
    news = News.objects.get(pk=news_id)
    if request.method == 'POST':
        form = NewsCreateUpdateForm(instance=news, data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('m_new_detail', args=[form.instance.id]))
        else:
            pass
    else:
        form = NewsCreateUpdateForm(instance=news)
    context = {
        'form': form,
        'news': news,
    }
    return render(request, 'sellerapp/new_edit.html', context)


def new_delete(request, news_id):
    news = News.objects.get(pk=news_id)
    news.delete()
    return HttpResponseRedirect(reverse('news_list'))


def quotes_list(request):
    quotes = Quote.objects.all()
    context = {
        'quotes': quotes
    }
    return render(request, 'sellerapp/quotes_list.html', context)


def quote_create(request):
    if request.method == 'POST':
        form = QuoteCreateUpdateForm(data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('m_quote_detail', args=[form.instance.id]))
    else:
        form = QuoteCreateUpdateForm()
    context = {
        'form': form,
    }
    return render(request, 'sellerapp/quote_create.html', context)


def quote_edit(request, quote_id):
    quote = Quote.objects.get(pk=quote_id)
    if request.method == 'POST':
        form = QuoteCreateUpdateForm(instance=quote, data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('m_quote_detail', args=[form.instance.id]))
        else:
            pass
    else:
        form = QuoteCreateUpdateForm(instance=quote)
    context = {
        'form': form,
        'quote': quote,
    }
    return render(request, 'sellerapp/quote_edit.html', context)


def quote_delete(request, quote_id):
    quote = Quote.objects.get(pk=quote_id)
    quote.delete()
    return HttpResponseRedirect(reverse('quotes_list'))


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


def m_quote_detail(request, quote_id):
    context = {
        'quote': Quote.objects.get(pk=quote_id)
    }
    return render(request, 'sellerapp/m_quote_detail.html', context)


def m_new_detail(request, news_id):
    context = {
        'news': News.objects.get(pk=news_id)
    }
    return render(request, 'sellerapp/m_new_detail.html', context)


def m_product_detail(request, book_id):
    context = {
        'book': Book.objects.get(pk=book_id)
    }
    return render(request, 'sellerapp/m_product_detail.html', context)


def order_list(request):
    return render(request, 'sellerapp/order_list.html')