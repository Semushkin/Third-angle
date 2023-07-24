from django.shortcuts import render, get_object_or_404
from mainapp.models import Book
from authapp.forms import UserRegisterForm, UserLoginForm, UserEditForm, SetNewPassword
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q

# Create your views here.


def index(request):
    context = {
        'books': Book.objects.all(),
    }
    return render(request, 'mainapp/index.html', context)


def catalog(request):
    object_list = Book.objects.all().order_by('id')
    items_per_page = 1
    paginator = Paginator(object_list, items_per_page)
    page_number = request.GET.get('page', 1)
    try:
        page_obj = paginator.get_page(page_number)
    except PageNotAnInteger:
        page_obj = paginator.get_page(1)
    except EmptyPage:
        page_obj = paginator.get_page(paginator.num_pages)
    context = {'page_obj': page_obj}
    return render(request, 'mainapp/catalog.html', context)


def search_result(request):
    object_list = Book.objects.all().order_by('id')
    query = request.GET.get('q')
    items_per_page = 1
    if query:
        object_list = Book.objects.filter(Q(name__iregex=query) | Q(author__iregex=query) | Q(price__iregex=query))
    paginator = Paginator(object_list, items_per_page)
    page_number = request.GET.get('page', 1)
    try:
        page_obj = paginator.get_page(page_number)
    except PageNotAnInteger:
        page_obj = paginator.get_page(1)
    except EmptyPage:
        page_obj = paginator.get_page(paginator.num_pages)
    context = {'object_list' : object_list, 'page_obj': page_obj}
    return render(request, 'mainapp/search_result.html', context)



def news(request):
    return render(request, 'mainapp/news.html')


def contacts(request):
    return render(request, 'mainapp/contact.html')


def about(request):
    return render(request, 'mainapp/about.html')


def rules(request):
    return render(request, 'mainapp/rules.html')


