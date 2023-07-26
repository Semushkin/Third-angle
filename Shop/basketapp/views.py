from django.shortcuts import render
from mainapp.models import Book
from authapp.forms import UserRegisterForm, UserLoginForm, UserEditForm, SetNewPassword
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from basketapp.models import Basket
from django.template.loader import render_to_string
from django.http import HttpResponseRedirect, JsonResponse


def search_detail(request):
    return render(request, 'basketapp/search_detail.html')


def order_detail(request):
    return render(request, 'basketapp/order_detail.html')


def cart(request):
    baskets = Basket.objects.filter(user=request.user)
    context = {
        'baskets': baskets,
    }
    return render(request, 'basketapp/cart.html', context)


def is_ajax(request):
    return request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest'


@login_required
def basket_add(request, book_id):
    if is_ajax(request=request):
        user = request.user
        book = Book.objects.get(id=book_id)
        baskets = Basket.objects.filter(user=user, book=book)

        if baskets:
            basket = baskets.first()
            basket.quantity += 1
            basket.save()
        else:
            Basket.objects.create(user=user, book=book, quantity=1)

        books = Book.objects.all()
        paginator = Paginator(Book.objects.all(), 1)
        page_number = request.GET.get('page', 1)
        page_obj = paginator.get_page(page_number)
        context = {'page_obj': page_obj}

        result = render_to_string('mainapp/includes/goods_card.html', context)
        return JsonResponse({'result': result})


@login_required
def basket_edit(request, basket_id, quantity):
    if is_ajax(request=request):
        basket = Basket.objects.get(id=basket_id)
        if quantity > 0:
            basket.quantity = quantity
            basket.save()
        else:
            basket.delete()

        baskets = Basket.objects.filter(user=request.user)
        context = {'baskets': baskets}

        result = render_to_string('basketapp/includes/basket.html', context)
        return JsonResponse({'result': result})


@login_required
def basket_remove(request, basket_id):
    Basket.objects.get(id=basket_id).delete()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))