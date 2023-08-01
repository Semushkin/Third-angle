from django.shortcuts import render
from mainapp.models import Book, News
from authapp.forms import UserRegisterForm, UserLoginForm, UserEditForm, SetNewPassword
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from mainapp.forms import BoorCreateUpdateForm
from django.db.models import Q


def s_order_detail(request):
    return render(request, 'sellerapp/s_order_detail.html')


def s_search_detail(request):
    return render(request, 'sellerapp/s_search_detail.html')


def search_list(request):
    return render(request, 'sellerapp/search_list.html')


def new_detail(request):
    return render(request, 'sellerapp/new_detail.html')


def product_detail(request, book_id):
    context = {
        'book': Book.objects.get(pk=book_id)
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
            Q(text__iregex=n_query)).order_by(
            request.session["n_sort"])
    else:
        if request.session["n_search"] == "":
            object_list = News.objects.order_by(request.session["n_sort"])
        else:
            object_list = News.objects.filter(
                Q(text__iregex=request.session["n_search"])).order_by(request.session["n_sort"])
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
        object_list = Book.objects.filter(Q(name__iregex=b_query) | Q(author__iregex=b_query) | Q(price__iregex=b_query)).order_by(request.session["b_sort"])
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
    context = {'object_list' : object_list, 'page_obj': page_obj, 'b_o_field': b_o_field, 'm_b_field': m_b_field}
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