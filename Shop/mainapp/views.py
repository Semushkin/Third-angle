from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, 'mainapp/index.html')


def catalog(request):
    return render(request, 'mainapp/shop.html')


def news(request):
    return render(request, 'mainapp/news.html')


def contacts(request):
    return render(request, 'mainapp/contact.html')


def about(request):
    return render(request, 'mainapp/about.html')


def cart(request):
    return render(request, 'mainapp/cart.html')


def edit_profile(request):
    return render(request, 'mainapp/edit_profile.html')


def login(request):
    return render(request, 'mainapp/login.html')


def order_detail(request):
    return render(request, 'mainapp/order_detail.html')


def order_list(request):
    return render(request, 'mainapp/order_list.html')


def profile(request):
    return render(request, 'mainapp/profile.html')


def registration(request):
    return render(request, 'mainapp/registration.html')


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
    return render(request, 'mainapp/single_new.html')


def product_detail(request):
    return render(request, 'mainapp/single_product.html')
