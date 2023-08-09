from django.shortcuts import render
from mainapp.models import Book
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from basketapp.models import Basket, Request, Order
from django.template.loader import render_to_string
from django.http import HttpResponseRedirect, JsonResponse
from basketapp.forms import RequestCreateForm


def search_detail(request, request_id):
    item = Request.objects.get(pk=request_id)
    context = {
        'request': item,
    }
    return render(request, 'basketapp/search_detail.html', context)


def search_create(request):
    if request.method == 'POST':
        text = request.POST.get('text')
        form = Request.objects.create(user=request.user, text=text)
        form.save()
        return HttpResponseRedirect(reverse('search_detail', args=[form.id]))
    else:
        form = RequestCreateForm()
    context = {
        'form': form,
    }
    return render(request, 'basketapp/search_create.html', context)


def order_detail(request, order_id):
    order = Order.objects.get(pk=order_id)
    baskets = Basket.objects.filter(order=order)
    context = {
        'baskets': baskets
    }
    return render(request, 'basketapp/order_detail.html', context)


def cart(request):
    baskets = Basket.objects.filter(user=request.user, order=None)
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
        baskets = Basket.objects.filter(user=user, book=book, order=None)

        if baskets:
            basket = baskets.first()
            basket.quantity += 1
            basket.save()
        else:
            Basket.objects.create(user=user, book=book, quantity=1)

        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


@login_required
def basket_edit(request, basket_id, quantity):
    if is_ajax(request=request):
        basket = Basket.objects.get(id=basket_id)
        if quantity > 0:
            basket.quantity = quantity
            basket.save()
        else:
            basket.delete()

        baskets = Basket.objects.filter(user=request.user, order=None)
        context = {'baskets': baskets}

        result = render_to_string('basketapp/includes/basket.html', context)
        return JsonResponse({'result': result})


@login_required
def basket_remove(request, basket_id):
    Basket.objects.get(id=basket_id).delete()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def ordered(request):
    baskets = Basket.objects.filter(user=request.user, order=None)
    order = Order.objects.create(user=request.user)
    for basket in baskets:
        basket.order = order
        basket.save()
    # return HttpResponseRedirect(reverse('cart'))
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


