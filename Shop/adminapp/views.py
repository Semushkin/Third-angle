import os

from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import user_passes_test
from django.urls import reverse

from authapp.models import User
from database import BookNew
from mainapp.forms import BoorCreateUpdateForm, ImagesForBookForm, AuthorForm, QuoteCreateUpdateForm, GenreForm, \
    NewsCreateUpdateForm
from mainapp.models import ImageBook, Authors, Quote, Genre, News


@user_passes_test(lambda u: u.is_superuser)
def admin_main(request):
    return render(request, 'adminapp/admin.html')


@user_passes_test(lambda u: u.is_superuser)
def admin_user_read(request):
    context = {
        'users': User.objects.all()
    }
    return render(request, 'adminapp/admin_user_read.html', context)


@user_passes_test(lambda u: u.is_superuser)
def admin_user_create(request):
    return render(request, 'adminapp/admin.html')


@user_passes_test(lambda u: u.is_superuser)
def admin_user_update_delete(request):
    return render(request, 'adminapp/admin.html')


@user_passes_test(lambda u: u.is_superuser)
def admin_book_read(request):
    context = {
        'books': BookNew.get_all_reverse()
    }
    return render(request, 'adminapp/admin_book_read.html', context)


@user_passes_test(lambda u: u.is_superuser)
def admin_book_create(request):
    if request.method == 'POST':
        form = BoorCreateUpdateForm(data=request.POST, files=request.FILES)

        if form.is_valid():
            book = BookNew.create(data=request.POST, files=request.FILES)
            if book:
                book_name = request.FILES['foto'].name
                request.FILES['foto'].name = book + os.path.splitext(book_name)[1]
                images_form = ImagesForBookForm(data={'guid': book}, files=request.FILES)
                if images_form.is_valid():
                    images_form.save()
                return HttpResponseRedirect(reverse('adminapp:admin_book_read'))
    else:
        form = BoorCreateUpdateForm()
    context = {
        'form': form,
    }
    return render(request, 'adminapp/admin_book_create.html', context)


@user_passes_test(lambda u: u.is_superuser)
def admin_book_update(request, book_id):
    if request.method == 'POST':
        form = BoorCreateUpdateForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            book = BookNew.update(data=request.POST, guid=book_id)
            if book:
                image = ImageBook.objects.filter(guid=book_id)
                if image:
                    images_form = ImagesForBookForm(instance=image.first(), data={'guid': book}, files=request.FILES)
                else:
                    images_form = ImagesForBookForm(data={'guid': book}, files=request.FILES)
                if images_form.is_valid():
                    images_form.save()
            return HttpResponseRedirect(reverse('adminapp:admin_book_read'))
        else:
            pass
    else:
        book = BookNew.get_by_guid(book_id)
        form = BoorCreateUpdateForm(data=book)
    context = {
        'form': form,
        'book': book,
    }
    return render(request, 'adminapp/admin_book_update_delete.html', context)


@user_passes_test(lambda u: u.is_superuser)
def admin_book_delete(request, book_id):
    BookNew.delete(book_id)
    return HttpResponseRedirect(reverse('adminapp:admin_book_read'))


@user_passes_test(lambda u: u.is_superuser)
def admin_author_read(request):
    context = {
        'authors': Authors.objects.all()
    }
    return render(request, 'adminapp/admin_author_read.html', context)


@user_passes_test(lambda u: u.is_superuser)
def admin_author_create(request):
    if request.method == 'POST':
        form = AuthorForm(data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('adminapp:admin_author_read'))
    else:
        form = AuthorForm()
    context = {
        'form': form,
    }
    return render(request, 'adminapp/admin_author_create.html', context)


@user_passes_test(lambda u: u.is_superuser)
def admin_author_update(request, author_id):
    author = Authors.objects.get(pk=author_id)
    if request.method == 'POST':
        form = AuthorForm(instance=author, data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('adminapp:admin_author_read'))
    else:
        form = AuthorForm(instance=author)
    context = {
        'form': form,
        'author': author
    }
    return render(request, 'adminapp/admin_author_update_delete.html', context)


@user_passes_test(lambda u: u.is_superuser)
def admin_author_delete(request, author_id):
    author = Authors.objects.get(pk=author_id)
    author.delete()
    return HttpResponseRedirect(reverse('adminapp:admin_author_read'))


@user_passes_test(lambda u: u.is_superuser)
def admin_genre_read(request):
    context = {
        'genres': Genre.objects.all()
    }
    return render(request, 'adminapp/admin_genre_read.html', context)


@user_passes_test(lambda u: u.is_superuser)
def admin_genre_create(request):
    if request.method == 'POST':
        form = GenreForm(data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('adminapp:admin_genre_read'))
    else:
        form = GenreForm()
    context = {
        'form': form,
    }
    return render(request, 'adminapp/admin_genre_create.html', context)


@user_passes_test(lambda u: u.is_superuser)
def admin_genre_update(request, genre_id):
    genre = Genre.objects.get(pk=genre_id)
    if request.method == 'POST':
        form = GenreForm(instance=genre, data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('adminapp:admin_genre_read'))
    else:
        form = GenreForm(instance=genre)
    context = {
        'form': form,
        'genre': genre
    }
    return render(request, 'adminapp/admin_genre_update_delete.html', context)


@user_passes_test(lambda u: u.is_superuser)
def admin_genre_delete(request, genre_id):
    genre = Genre.objects.get(pk=genre_id)
    genre.delete()
    return HttpResponseRedirect(reverse('adminapp:admin_genre_read'))


@user_passes_test(lambda u: u.is_superuser)
def admin_quote_read(request):
    context = {
        'quotes': Quote.objects.all()
    }
    return render(request, 'adminapp/admin_quote_read.html', context)


@user_passes_test(lambda u: u.is_superuser)
def admin_quote_create(request):
    if request.method == 'POST':
        form = QuoteCreateUpdateForm(data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('adminapp:admin_quote_read'))
    else:
        form = QuoteCreateUpdateForm()
    context = {
        'form': form,
    }
    return render(request, 'adminapp/admin_quote_create.html', context)


@user_passes_test(lambda u: u.is_superuser)
def admin_quote_update(request, quote_id):
    quote = Quote.objects.get(pk=quote_id)
    if request.method == 'POST':
        form = QuoteCreateUpdateForm(instance=quote, data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('adminapp:admin_quote_read'))
    else:
        form = QuoteCreateUpdateForm(instance=quote)
    context = {
        'form': form,
        'quote': quote
    }
    return render(request, 'adminapp/admin_quote_update_delete.html', context)


@user_passes_test(lambda u: u.is_superuser)
def admin_quote_delete(request, quote_id):
    quote = Quote.objects.get(pk=quote_id)
    quote.delete()
    return HttpResponseRedirect(reverse('adminapp:admin_quote_read'))


@user_passes_test(lambda u: u.is_superuser)
def admin_new_read(request):
    context = {
        'news': News.objects.all()
    }
    return render(request, 'adminapp/admin_new_read.html', context)


@user_passes_test(lambda u: u.is_superuser)
def admin_new_create(request):
    if request.method == 'POST':
        form = NewsCreateUpdateForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('adminapp:admin_new_read'))
    else:
        form = NewsCreateUpdateForm()
    context = {
        'form': form,
    }
    return render(request, 'adminapp/admin_new_create.html', context)


@user_passes_test(lambda u: u.is_superuser)
def admin_new_update(request, new_id):
    news = News.objects.get(pk=new_id)
    if request.method == 'POST':
        form = NewsCreateUpdateForm(instance=news, data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('adminapp:admin_new_read'))
        else:
            pass
    else:
        form = NewsCreateUpdateForm(instance=news)
    context = {
        'form': form,
        'news': news,
    }
    return render(request, 'adminapp/admin_new_update_delete.html', context)


@user_passes_test(lambda u: u.is_superuser)
def admin_new_delete(request, new_id):
    news = News.objects.get(pk=new_id)
    news.delete()
    return HttpResponseRedirect(reverse('adminapp:admin_new_read'))


@user_passes_test(lambda u: u.is_superuser)
def admin_news_read(request):
    pass


@user_passes_test(lambda u: u.is_superuser)
def admin_comment_read(request):
    pass


@user_passes_test(lambda u: u.is_superuser)
def admin_basket_read(request):
    pass


@user_passes_test(lambda u: u.is_superuser)
def admin_order_read(request):
    pass

