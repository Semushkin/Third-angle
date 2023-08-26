from django.shortcuts import render
from mainapp.models import Book, News, Quote, Comment, ImageBook, Authors, Genre
from authapp.forms import UserRegisterForm, UserLoginForm, UserEditForm, SetNewPassword
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q, Sum
from mainapp.forms import BoorCreateUpdateForm, NewsCreateUpdateForm, QuoteCreateUpdateForm, CommentCreateUpdateForm, ImagesForBookForm
from basketapp.models import Request, Order, Basket
from basketapp.forms import RequestCreateForm, RequestUpdateForm, OrderStatusChangeForm
from database import BookNew
import os
from django.views.generic import ListView


def s_order_detail(request, order_id):
    order = Order.objects.get(pk=order_id)
    baskets = Basket.objects.filter(order=order)
    if request.method == 'POST':
        form = OrderStatusChangeForm(instance=order, data=request.POST)
        if form.is_valid():
            form.save()
    else:
        form = OrderStatusChangeForm(instance=order)
    context = {
        'baskets': baskets,
        'order': order,
        'form': form
    }
    return render(request, 'sellerapp/s_order_detail.html', context)


def s_search_detail(request, request_id):
    item = Request.objects.get(pk=request_id)
    if request.method == 'POST':
        form = RequestUpdateForm(instance=item, data=request.POST)
        form.save()

    else:
        form = RequestUpdateForm(instance=item)
    context = {
        'request': item, 'form': form,
    }
    return render(request, 'sellerapp/s_search_detail.html', context)


def search_list(request):
    if "s_sort" not in request.session:
        request.session["s_sort"] = "id"
    if "s_search" not in request.session:
        request.session["s_search"] = ""
    if "s_filter" not in request.session:
        request.session["s_filter"] = ""
    s_order = request.GET.get('s_sort')
    s_filter = request.GET.get('s_filter')
    if s_order:
        request.session["s_sort"] = s_order
    if s_filter:
        request.session["s_filter"] = s_filter
    s_query = request.GET.get('s_q')
    stop = request.GET.get('stop_search')
    stop_f = request.GET.get('stop_filter')
    if stop:
        request.session["s_search"] = ""
    if stop_f:
        request.session["s_filter"] = ""
    s_o_field = request.session["s_sort"]
    s_f_field = request.session["s_filter"]
    if s_filter:
        request.session["s_filter"] = s_filter
        if request.session["s_search"] == "":
            object_list = Request.objects.filter(
                Q(status__iregex=request.session["s_filter"])).order_by(request.session["s_sort"])
        else:
            object_list = Request.objects.filter(Q(status__iregex=request.session["s_filter"])).filter(
                Q(text__iregex=request.session["s_search"]) | Q(id__iregex=request.session["o_search"]) | Q(
                    create_date__iregex=request.session["s_search"])).order_by(request.session["s_sort"])
    elif s_query:
        request.session["s_search"] = s_query
        if request.session["s_filter"] == "":
            object_list = Request.objects.filter(
                Q(text__iregex=request.session["s_search"]) | Q(id__iregex=request.session["o_search"]) | Q(
                    create_date__iregex=request.session["s_search"])).order_by(request.session["s_sort"])
        else:
            object_list = Request.objects.filter(Q(status__iregex=request.session["s_filter"])).filter(
                Q(text__iregex=request.session["s_search"]) | Q(id__iregex=request.session["o_search"]) | Q(
                    create_date__iregex=request.session["s_search"])).order_by(request.session["s_sort"])
    else:
        if request.session["s_search"] == "":
            if request.session["s_filter"] == "":
                object_list = Request.objects.order_by(request.session["s_sort"])
            else:
                object_list = Request.objects.filter(
                    Q(status__iregex=request.session["s_filter"])).order_by(request.session["s_sort"])
        else:
            if request.session["s_filter"] == "":
                object_list = Request.objects.filter(
                    Q(text__iregex=request.session["s_search"]) | Q(id__iregex=request.session["o_search"]) | Q(
                        create_date__iregex=request.session["s_search"])).order_by(request.session["s_sort"])
            else:
                object_list = Request.objects.filter(Q(status__iregex=request.session["s_filter"])).filter(
                    Q(text__iregex=request.session["s_search"]) | Q(id__iregex=request.session["o_search"]) | Q(
                        create_date__iregex=request.session["s_search"])).order_by(request.session["s_sort"])

    s_s_field = request.session["s_search"]
    items_per_page = 1
    paginator = Paginator(object_list, items_per_page)
    page_number = request.GET.get('page', 1)
    try:
        page_obj = paginator.get_page(page_number)
    except PageNotAnInteger:
        page_obj = paginator.get_page(1)
    except EmptyPage:
        page_obj = paginator.get_page(paginator.num_pages)
    context = {'object_list': object_list, 'page_obj': page_obj, 's_f_field': s_f_field, 's_o_field': s_o_field, 's_s_field': s_s_field}
    return render(request, 'sellerapp/search_list.html', context)


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
            book = BookNew.create(data=request.POST, files=request.FILES)
            if book:

                #-----------Проверяем автора и записываем при необходимости.
                all_new_authors = request.POST['author'].split(',')
                all_authors_base = Authors.objects.all()
                for new_author in all_new_authors:
                    write = True
                    for author_base in all_authors_base:
                        if new_author == author_base.person:
                            write = False
                            break
                    if write:
                        author = Authors.objects.create(person=new_author)
                        author.save()
                #-----------------------------------------------------------

                # -----------Проверяем жанр и записываем при необходимости.
                all_new_categories = request.POST['category'].split(',')
                all_category_base = Genre.objects.all()
                for new_category in all_new_categories:
                    write = True
                    for category_base in all_category_base:
                        if new_category == category_base.category:
                            write = False
                            break
                    if write:
                        genre = Genre.objects.create(category=new_category)
                        genre.save()
                # -----------------------------------------------------------

                book_name = request.FILES['foto'].name
                request.FILES['foto'].name = book + os.path.splitext(book_name)[1]
                images_form = ImagesForBookForm(data={'guid': book}, files=request.FILES)
                if images_form.is_valid():
                    images_form.save()
                return HttpResponseRedirect(reverse('m_product_detail', args=[book]))
    else:
        form = BoorCreateUpdateForm()
    context = {
        'form': form,
    }
    return render(request, 'sellerapp/product_create.html', context)


def product_edit(request, book_id):
    if request.method == 'POST':
        form = BoorCreateUpdateForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            book = BookNew.update(data=request.POST, guid=book_id)
            if book:
                image = ImageBook.objects.filter(guid=book_id)
                if image:
                    images_form = ImagesForBookForm(instance=image.first(), data={'guid': book}, files=request.FILES)
                else:
                    images_form = ImagesForBookForm(data={'guid': book}, files=request.FILES)
                if images_form.is_valid():
                    images_form.save()
            return HttpResponseRedirect(reverse('m_product_detail', args=[book]))
        else:
            pass
    else:
        book = BookNew.get_by_guid(book_id)
        form = BoorCreateUpdateForm(data=book)
    context = {
        'form': form,
        'book': book,
    }
    return render(request, 'sellerapp/product_edit.html', context)


def product_delete(request, book_id):
    # book = Book.objects.get(pk=book_id)
    # book.delete()
    BookNew.delete(book_id)
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
        'book': BookNew.get_by_guid(book_id)
    }
    return render(request, 'sellerapp/m_product_detail.html', context)


def order_list(request):
    if "o_sort" not in request.session:
        request.session["o_sort"] = "id"
    if "o_search" not in request.session:
        request.session["o_search"] = ""
    if "o_filter" not in request.session:
        request.session["o_filter"] = ""
    o_order = request.GET.get('o_sort')
    o_filter = request.GET.get('o_filter')
    if o_order:
        request.session["o_sort"] = o_order
    if o_filter:
        request.session["o_filter"] = o_filter
    o_query = request.GET.get('o_q')
    stop = request.GET.get('stop_search')
    stop_f = request.GET.get('stop_filter')
    if stop:
        request.session["o_search"] = ""
    if stop_f:
        request.session["o_filter"] = ""
    o_o_field = request.session["o_sort"]
    o_f_field = request.session["o_filter"]
    if o_filter:
        request.session["o_filter"] = o_filter
        if request.session["o_search"] == "":
            object_list = Order.objects.filter(
                Q(status__iregex=request.session["o_filter"])).order_by(request.session["o_sort"])
        else:
            object_list = Order.objects.filter(Q(status__iregex=request.session["o_filter"])).filter(
                Q(basket__book__name__iregex=request.session["o_search"]) | Q(user__username__contains=request.session["o_search"]) | Q(id__iregex=request.session["o_search"]) | Q(
                    create_date__iregex=request.session["o_search"])).order_by(request.session["o_sort"])
    elif o_query:
        request.session["o_search"] = o_query
        if request.session["o_filter"] == "":
            object_list = Order.objects.filter(
                Q(basket__book__name__iregex=request.session["o_search"]) | Q(user__username__contains=request.session["o_search"]) | Q(id__iregex=request.session["o_search"]) | Q(
                    create_date__iregex=request.session["o_search"])).order_by(request.session["o_sort"])
        else:
            object_list = Order.objects.filter(Q(status__iregex=request.session["o_filter"])).filter(
                Q(basket__book__name__iregex=request.session["o_search"]) | Q(user__username__contains=request.session["o_search"]) | Q(id__iregex=request.session["o_search"]) | Q(
                    create_date__iregex=request.session["o_search"])).order_by(request.session["o_sort"])
    else:
        if request.session["o_search"] == "":
            if request.session["o_filter"] == "":
                object_list = Order.objects.order_by(request.session["o_sort"])
            else:
                object_list = Order.objects.filter(
                    Q(status__iregex=request.session["o_filter"])).order_by(request.session["o_sort"])
        else:
            if request.session["o_filter"] == "":
                object_list = Order.objects.filter(
                    Q(basket__book__name__iregex=request.session["o_search"]) | Q(user__username__contains=request.session["o_search"]) | Q(id__iregex=request.session["o_search"]) | Q(
                        create_date__iregex=request.session["o_search"])).order_by(request.session["o_sort"])
            else:
                object_list = Order.objects.filter(Q(status__iregex=request.session["o_filter"])).filter(
                    Q(basket__book__name__iregex=request.session["o_search"]) | Q(user__username__contains=request.session["o_search"]) | Q(id__iregex=request.session["o_search"]) | Q(
                        create_date__iregex=request.session["o_search"])).order_by(request.session["o_sort"])

    s_o_field = request.session["o_search"]
    items_per_page = 1
    paginator = Paginator(object_list, items_per_page)
    page_number = request.GET.get('page', 1)
    try:
        page_obj = paginator.get_page(page_number)
    except PageNotAnInteger:
        page_obj = paginator.get_page(1)
    except EmptyPage:
        page_obj = paginator.get_page(paginator.num_pages)
    context = {'object_list': object_list, 'page_obj': page_obj, 'o_f_field': o_f_field, 'o_o_field': o_o_field,
               's_o_field': s_o_field}
    return render(request, 'sellerapp/order_list.html', context)


