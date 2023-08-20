from django.shortcuts import render

from database import UserNew
from mainapp.models import Book
from basketapp.models import Order
from authapp.forms import UserRegisterForm, UserLoginForm, UserEditForm, SetNewPassword, UserDataCreateUpdateForm
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from basketapp.models import Request


@login_required
def edit_profile(request):
    error = False
    if request.method == 'POST':
        form = UserEditForm(instance=request.user, data=request.POST)
        form_pass = SetNewPassword(request.user, data=request.POST)
        if form.is_valid():
            form.save()
            if request.POST.get('new_password1'):
                if form_pass.is_valid():
                    form_pass.save()
                else:
                    print(f'Ошибка редактирования формы профиля пользователя "{form_pass.errors}"')
                    error = True
            if not error:
                return HttpResponseRedirect(reverse('profile'))
        else:
            print(f'Ошибка редактирования формы профиля пользователя "{form.errors}"')
    else:
        form = UserEditForm(instance=request.user)
        form_pass = SetNewPassword(request.user)
    context = {
        'form': form,
        'form_pass': form_pass,
    }
    return render(request, 'authapp/profile_edit.html', context)


def login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = auth.authenticate(username=username, password=password)
            # auth.login(request, user)
            if user.is_active:
                auth.login(request, user)
                return HttpResponseRedirect(reverse('index'))
        else:
            print(f'Ошибка формы авторизации "{form.errors}"')
    else:
        form = UserLoginForm()

    context = {
        'form': form
    }

    return render(request, 'authapp/login.html', context)


@login_required
def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('index'))


@login_required
def profile(request):
    requests = Request.objects.filter(user=request.user)
    orders = Order.objects.filter(user=request.user)
    context = {
            'requests': requests,
            'orders': orders
        }
    return render(request, 'authapp/profile.html', context)


def registration(request):
    if request.method == 'POST':
        form = UserRegisterForm(data=request.POST)
        if form.is_valid():
            form.save()
            user_data = UserNew.create(data=request.POST, user_id=[form.instance.id])
            return HttpResponseRedirect(reverse('index'))
        else:
            print(f'Ошибка формы регистрации формы "{form.errors}"')
    else:
        form = UserRegisterForm()
    context = {
        'form': form,
        'form_data': UserDataCreateUpdateForm()
    }
    return render(request, 'authapp/registration.html', context)