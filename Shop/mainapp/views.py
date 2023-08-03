from django.shortcuts import render, get_object_or_404
from mainapp.models import Book, BookCategory, News, Quote
from authapp.forms import UserRegisterForm, UserLoginForm, UserEditForm, SetNewPassword
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q
import random

# Create your views here.


def index(request):

    context = {
        'books': Book.objects.order_by('-id'), 'main_books': Book.objects.order_by('?'), 'news': News.objects.order_by('-id'), 'quotes': Quote.objects.all()
    }
    return render(request, 'mainapp/index.html', context)


def catalog(request):
    if "sort" not in request.session:
        request.session["sort"] = "id"
    if "filt" not in request.session:
        request.session["filt"] = "все"
    filt = request.GET.get('filt')
    order = request.GET.get('sort')
    if filt:
        request.session["filt"] = filt
    if order:
        request.session["sort"] = order
    f_filed = request.session["filt"]
    o_field = request.session["sort"]
    if f_filed == "все":
        object_list = Book.objects.all().order_by(request.session["sort"])
    else:
        object_list = Book.objects.all().order_by(request.session["sort"]).filter(
            Q(author__icontains=request.session["filt"]) | Q(category__name__icontains=request.session["filt"]))
    genre = BookCategory.objects.all()
    items_per_page = 1
    paginator = Paginator(object_list, items_per_page)
    page_number = request.GET.get('page', 1)
    try:
        page_obj = paginator.get_page(page_number)
    except PageNotAnInteger:
        page_obj = paginator.get_page(1)
    except EmptyPage:
        page_obj = paginator.get_page(paginator.num_pages)
    context = {'page_obj': page_obj, 'f_filed': f_filed, 'o_field': o_field, 'genre': genre}
    return render(request, 'mainapp/catalog.html', context)


def search_result(request):
    if "sort" not in request.session:
        request.session["sort"] = "id"
    if "search" not in request.session:
        request.session["search"] = ""
    order = request.GET.get('sort')
    if order:
        request.session["sort"] = order
    o_field = request.session["sort"]
    query = request.GET.get('q')
    items_per_page = 1
    if query:
        request.session["search"] = query
        object_list = Book.objects.filter(Q(name__iregex=query) | Q(author__iregex=query) | Q(price__iregex=query)).order_by(request.session["sort"])
    else:
        object_list = Book.objects.filter(
            Q(name__iregex=request.session["search"]) | Q(author__iregex=request.session["search"]) | Q(price__iregex=request.session["search"])).order_by(request.session["sort"])
    paginator = Paginator(object_list, items_per_page)
    page_number = request.GET.get('page', 1)
    try:
        page_obj = paginator.get_page(page_number)
    except PageNotAnInteger:
        page_obj = paginator.get_page(1)
    except EmptyPage:
        page_obj = paginator.get_page(paginator.num_pages)
    context = {'object_list' : object_list, 'page_obj': page_obj, 'o_field': o_field}
    return render(request, 'mainapp/search_result.html', context)



def news(request):
    object_list = News.objects.order_by('-date_create')
    items_per_page = 2
    paginator = Paginator(object_list, items_per_page)
    page_number = request.GET.get('page', 1)
    try:
        page_obj = paginator.get_page(page_number)
    except PageNotAnInteger:
        page_obj = paginator.get_page(1)
    except EmptyPage:
        page_obj = paginator.get_page(paginator.num_pages)
    context = {'page_obj': page_obj}
    return render(request, 'mainapp/news.html', context)


def contacts(request):
    return render(request, 'mainapp/contact.html')


def about(request):
    return render(request, 'mainapp/about.html')


def rules(request):
    return render(request, 'mainapp/rules.html')


