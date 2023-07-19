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


def cart(request):
    return render(request, 'mainapp/cart.html')


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
    return render(request, 'mainapp/profile_edit.html', context)


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

    return render(request, 'mainapp/login.html', context)


@login_required
def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('index'))


def order_detail(request):
    return render(request, 'mainapp/order_detail.html')


def order_list(request):
    return render(request, 'mainapp/order_list.html')


@login_required
def profile(request):
    return render(request, 'mainapp/profile.html')


def registration(request):
    if request.method == 'POST':
        form = UserRegisterForm(data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('index'))
        else:
            print(f'Ошибка формы регистрации формы "{form.errors}"')
    else:
        form = UserRegisterForm()
    context = {
     'form': form
    }
    return render(request, 'mainapp/registration.html', context)


def rules(request):
    return render(request, 'mainapp/rules.html')


def s_order_detail(request):
    return render(request, 'mainapp/s_order_detail.html')


def s_search_detail(request):
    return render(request, 'mainapp/s_search_detail.html')


def search_detail(request):
    return render(request, 'mainapp/search_detail.html')


def search_list(request):
    return render(request, 'mainapp/search_list.html')


def new_detail(request):
    return render(request, 'mainapp/new_detail.html')


def product_detail(request):
    return render(request, 'mainapp/product_detail.html')


def m_profile(request):
    return render(request, 'mainapp/m_profile.html')


def s_profile(request):
    return render(request, 'mainapp/s_profile.html')


def news_list(request):
    return render(request, 'mainapp/news_list.html')


def new_create(request):
    return render(request, 'mainapp/new_create.html')


def new_edit(request):
    return render(request, 'mainapp/new_edit.html')


def quotes_list(request):
    return render(request, 'mainapp/quotes_list.html')


def quote_create(request):
    return render(request, 'mainapp/quote_create.html')


def quote_edit(request):
    return render(request, 'mainapp/quote_edit.html')


def products_list(request):
    context = {
        'books': Book.objects.all(),
    }
    return render(request, 'mainapp/products_list.html', context)


def product_create(request):
    return render(request, 'mainapp/product_create.html')


def product_edit(request):
    return render(request, 'mainapp/product_edit.html')


def m_quote_detail(request):
    return render(request, 'mainapp/m_quote_detail.html')


def m_new_detail(request):
    return render(request, 'mainapp/m_new_detail.html')


def m_product_detail(request):
    return render(request, 'mainapp/m_product_detail.html')

