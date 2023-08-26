from django.shortcuts import render

from authapp.models import User
from database import UserNew
from mainapp.models import Book
from basketapp.models import Order
from authapp.forms import UserRegisterForm, UserLoginForm, UserEditForm, SetNewPassword, UserDataForm
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
        form_data = UserDataForm(data=request.POST)
        if form.is_valid() and form_data.is_valid():
            form.save()
            updated_data = UserNew.update(data=request.POST, guid=request.user.guid)
            if not updated_data:
                user_guid = UserNew.create(data=request.POST)
                if user_guid:
                    user = User.objects.get(id=request.user.pk)
                    user.guid = user_guid
                    user.save()
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

        user_data = UserNew.get_by_guid(request.user.guid)

        if user_data:
            form_data = UserDataForm(data=user_data)
        else:
            form_data = UserDataForm()

        form = UserEditForm(instance=request.user)
        form_pass = SetNewPassword(request.user)
    context = {
        'form': form,
        'form_pass': form_pass,
        'form_data': form_data
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
    user_data = UserNew.get_by_guid(request.user.guid)
    context = {
            'requests': requests,
            'orders': orders,
            'user_data': user_data
        }
    return render(request, 'authapp/profile.html', context)


def registration(request):
    if request.method == 'POST':
        main_form = UserRegisterForm(data=request.POST)
        data_form = UserDataForm(data=request.POST)

        if main_form.is_valid() and data_form.is_valid():
            user_data = UserNew.create(data=request.POST)
            if user_data:
                main_form.save()

                user = User.objects.get(id=main_form.instance.id)
                user.guid = user_data
                user.save()
            return HttpResponseRedirect(reverse('index'))
        else:
            print(f'Ошибка формы регистрации формы "{main_form.errors}"')
    else:
        main_form = UserRegisterForm()
        data_form = UserDataForm()
    context = {
        'main_form': main_form,
        'data_form': data_form
    }
    return render(request, 'authapp/registration.html', context)