from django.shortcuts import render
from mainapp.models import Book
from authapp.forms import UserRegisterForm, UserLoginForm, UserEditForm, SetNewPassword
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator


def search_detail(request):
    return render(request, 'basketapp/search_detail.html')


def order_detail(request):
    return render(request, 'basketapp/order_detail.html')


def cart(request):
    return render(request, 'basketapp/cart.html')