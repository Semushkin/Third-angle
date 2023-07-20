from django.shortcuts import render
from mainapp.models import Book
from authapp.forms import UserRegisterForm, UserLoginForm, UserEditForm, SetNewPassword
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator

# Create your views here.


def index(request):
    context = {
        'books': Book.objects.all(),
    }
    return render(request, 'mainapp/index.html', context)


def catalog(request):
    object_list = Book.objects.all()
    items_per_page = 1
    paginator = Paginator(object_list, items_per_page)
    page_number = request.GET.get('page', 1)
    page_obj = paginator.get_page(page_number)
    context = {'page_obj': page_obj}
    return render(request, 'mainapp/catalog.html', context)



def news(request):
    return render(request, 'mainapp/news.html')


def contacts(request):
    return render(request, 'mainapp/contact.html')


def about(request):
    return render(request, 'mainapp/about.html')


def rules(request):
    return render(request, 'mainapp/rules.html')


