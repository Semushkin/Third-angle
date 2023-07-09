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
