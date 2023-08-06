from django.shortcuts import render
from mainapp.models import Book, News, Quote, Comment
from authapp.forms import UserRegisterForm, UserLoginForm, UserEditForm, SetNewPassword
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q
from mainapp.forms import BoorCreateUpdateForm, NewsCreateUpdateForm, QuoteCreateUpdateForm, CommentCreateUpdateForm


def s_order_detail(request):
    return render(request, 'sellerapp/s_order_detail.html')


def s_search_detail(request):
    return render(request, 'sellerapp/s_search_detail.html')


def search_list(request):
    return render(request, 'sellerapp/search_list.html')


def new_detail(request, new_id):
    context = {
        'new': News.objects.get(pk=new_id)
    }
    return render(request, 'sellerapp/new_detail.html', context)


def product_detail(request, book_id):
    book = Book.objects.get(pk=book_id)
    comment = Comment.objects.filter(book=book_id)

    if request.user.is_anonymous:
        context = {
            'book': book, 'comment': comment
        }
    else:
        comment_valid = Comment.objects.filter(book=book_id, user=request.user)
        if comment_valid:
            context = {
                'book': book, 'comment': comment
            }
        else:
            if request.method == 'POST':
                starts = request.POST.get('starts')
                text = request.POST.get('text')
                form = Comment.objects.create(book=Book.objects.get(pk=book_id), user=request.user, text=text,
                                              starts=starts)
                form.save()
                return HttpResponseRedirect(reverse('product_detail', args=[book_id]))
            else:
                form = CommentCreateUpdateForm()
            context = {
                'form': form, 'book': book, 'comment': comment
            }
    return render(request, 'sellerapp/product_detail.html', context)


def m_profile(request):
    return render(request, 'sellerapp/m_profile.html')


def s_profile(request):
    return render(request, 'sellerapp/s_profile.html')


def news_list(request):
    if "n_sort" not in request.session:
        request.session["n_sort"] = "id"
    if "n_search" not in request.session:
        request.session["n_search"] = ""
    n_order = request.GET.get('n_sort')
    if n_order:
        request.session["n_sort"] = n_order
    n_o_field = request.session["n_sort"]
    n_query = request.GET.get('n_q')
    stop = request.GET.get('stop_search')
    if stop:
        request.session["n_search"] = ""
    if n_query:
        request.session["n_search"] = n_query
        object_list = News.objects.filter(
            Q(name__iregex=n_query) | Q(text__iregex=n_query) | Q(description__iregex=n_query)).order_by(
            request.session["n_sort"])
    else:
        if request.session["n_search"] == "":
            object_list = News.objects.order_by(request.session["n_sort"])
        else:
            object_list = News.objects.filter(
                Q(name__iregex=request.session["n_search"]) | Q(text__iregex=request.session["n_search"]) | Q(
                    description__iregex=request.session["n_search"])).order_by(request.session["n_sort"])
    m_n_field = request.session["n_search"]
    items_per_page = 1
    paginator = Paginator(object_list, items_per_page)
    page_number = request.GET.get('page', 1)
    try:
        page_obj = paginator.get_page(page_number)
    except PageNotAnInteger:
        page_obj = paginator.get_page(1)
    except EmptyPage:
        page_obj = paginator.get_page(paginator.num_pages)
    context = {'object_list': object_list, 'page_obj': page_obj, 'n_o_field': n_o_field, 'm_n_field': m_n_field}
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
    if "q_sort" not in request.session:
        request.session["q_sort"] = "id"
    if "q_search" not in request.session:
        request.session["q_search"] = ""
    q_order = request.GET.get('q_sort')
    if q_order:
        request.session["q_sort"] = q_order
    q_o_field = request.session["q_sort"]
    q_query = request.GET.get('q_q')
    stop = request.GET.get('stop_search')
    if stop:
        request.session["q_search"] = ""
    if q_query:
        request.session["q_search"] = q_query
        object_list = Quote.objects.filter(
            Q(name__iregex=q_query) | Q(text__iregex=q_query) | Q(author__iregex=q_query)).order_by(
            request.session["q_sort"])
    else:
        if request.session["q_search"] == "":
            object_list = Quote.objects.order_by(request.session["q_sort"])
        else:
            object_list = Quote.objects.filter(
                Q(name__iregex=request.session["q_search"]) | Q(text__iregex=request.session["q_search"]) | Q(
                    author__iregex=request.session["q_search"])).order_by(request.session["q_sort"])
    m_q_field = request.session["q_search"]
    items_per_page = 1
    paginator = Paginator(object_list, items_per_page)
    page_number = request.GET.get('page', 1)
    try:
        page_obj = paginator.get_page(page_number)
    except PageNotAnInteger:
        page_obj = paginator.get_page(1)
    except EmptyPage:
        page_obj = paginator.get_page(paginator.num_pages)
    context = {'object_list': object_list, 'page_obj': page_obj, 'q_o_field': q_o_field, 'm_q_field': m_q_field}
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
    if "b_sort" not in request.session:
        request.session["b_sort"] = "id"
    if "b_search" not in request.session:
        request.session["b_search"] = ""
    b_order = request.GET.get('b_sort')
    if b_order:
        request.session["b_sort"] = b_order
    b_o_field = request.session["b_sort"]
    b_query = request.GET.get('b_q')
    stop = request.GET.get('stop_search')
    if stop:
        request.session["b_search"] = ""
    if b_query:
        request.session["b_search"] = b_query
        object_list = Book.objects.filter(
            Q(name__iregex=b_query) | Q(author__iregex=b_query) | Q(price__iregex=b_query)).order_by(
            request.session["b_sort"])
    else:
        if request.session["b_search"] == "":
            object_list = Book.objects.order_by(request.session["b_sort"])
        else:
            object_list = Book.objects.filter(
                Q(name__iregex=request.session["b_search"]) | Q(author__iregex=request.session["b_search"]) | Q(
                    price__iregex=request.session["b_search"])).order_by(request.session["b_sort"])
    m_b_field = request.session["b_search"]
    items_per_page = 1
    paginator = Paginator(object_list, items_per_page)
    page_number = request.GET.get('page', 1)
    try:
        page_obj = paginator.get_page(page_number)
    except PageNotAnInteger:
        page_obj = paginator.get_page(1)
    except EmptyPage:
        page_obj = paginator.get_page(paginator.num_pages)
    context = {'object_list': object_list, 'page_obj': page_obj, 'b_o_field': b_o_field, 'm_b_field': m_b_field}
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
        form = BoorCreateUpdateForm(instance=book, data=request.POST, files=request.FILES)
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
