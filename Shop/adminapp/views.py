import os

from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import user_passes_test
from django.urls import reverse

from authapp.forms import UserRegisterForm, UserDataForm, SetNewPassword, UserEditForm
from authapp.models import User
from database import BookNew, NewsNew, UserNew
from mainapp.forms import BoorCreateUpdateForm, ImagesForBookForm, AuthorForm, QuoteCreateUpdateForm, GenreForm, \
    NewsCreateUpdateForm, ImagesForNewsForm
from mainapp.models import ImageBook, Authors, Quote, Genre


@user_passes_test(lambda u: u.is_superuser)
def admin_main(request):
    return render(request, 'adminapp/admin.html')


@user_passes_test(lambda u: u.is_superuser)
def admin_user_read(request):

    users_shop = User.objects.all()
    users_data = UserNew.get_all()
    users = []
    for user_shop in users_shop:
        user = {
            'username': user_shop.username,
            'pk': user_shop.pk
        }
        for user_data in users_data:
            if user_shop.guid == user_data['id']:
                user.update(user_data)
                continue
        users.append(user)

    context = {
        'users': users,
        # 'users_data': UserNew.get_all()
    }
    return render(request, 'adminapp/admin_user_read.html', context)


@user_passes_test(lambda u: u.is_superuser)
def admin_user_create(request):
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

            return HttpResponseRedirect(reverse('adminapp:admin_user_read'))
    else:
        main_form = UserRegisterForm()
        data_form = UserDataForm()
    context = {
        'main_form': main_form,
        'data_form': data_form
    }
    return render(request, 'adminapp/admin_user_create.html', context)


@user_passes_test(lambda u: u.is_superuser)
def admin_user_update(request, user_pk):
    user = User.objects.get(pk=user_pk)
    if request.method == 'POST':
        main_form = UserEditForm(instance=user, data=request.POST)
        data_form = UserDataForm(data=request.POST)
        if main_form.is_valid() and data_form.is_valid():
            main_form.save()
            updated_data = UserNew.update(data=request.POST, guid=user.guid)
            if not updated_data:
                user_guid = UserNew.create(data=request.POST)
                if user_guid:
                    user.guid = user_guid
                    user.save()
            return HttpResponseRedirect(reverse('adminapp:admin_user_read'))
    else:
        user_data = UserNew.get_by_guid(user.guid)
        if user_data:
            data_form = UserDataForm(data=user_data)
        else:
            data_form = UserDataForm()
        main_form = UserEditForm(instance=user)
    context = {
        'main_form': main_form,
        'data_form': data_form,
        'user': user
    }
    return render(request, 'adminapp/admin_user_update_delete.html', context)


@user_passes_test(lambda u: u.is_superuser)
def admin_user_delete(request, user_id):
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
def admin_news_read(request):
    context = {
        'all_news': NewsNew.get_all_reverse()
    }
    return render(request, 'adminapp/admin_news_read.html', context)


@user_passes_test(lambda u: u.is_superuser)
def admin_news_create(request):
    if request.method == 'POST':
        form = NewsCreateUpdateForm(data=request.POST, files=request.FILES)

        if form.is_valid():
            news = NewsNew.create(data=request.POST)
            if news:
                news_name = request.FILES['foto'].name
                request.FILES['foto'].name = news + os.path.splitext(news_name)[1]
                images_form = ImagesForNewsForm(data={'guid': news}, files=request.FILES)
                if images_form.is_valid():
                    images_form.save()
                return HttpResponseRedirect(reverse('adminapp:admin_news_read'))
    else:
        form = NewsCreateUpdateForm()
    context = {
        'form': form,
    }
    return render(request, 'adminapp/admin_news_create.html', context)


@user_passes_test(lambda u: u.is_superuser)
def admin_news_update(request, news_id):
    if request.method == 'POST':
        form = NewsCreateUpdateForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            news = NewsNew.update(data=request.POST, guid=news_id)
            if news:
                image = ImageBook.objects.filter(guid=news_id)
                if image:
                    images_form = ImagesForBookForm(instance=image.first(), data={'guid': news}, files=request.FILES)
                else:
                    images_form = ImagesForBookForm(data={'guid': news}, files=request.FILES)
                if images_form.is_valid():
                    images_form.save()
            return HttpResponseRedirect(reverse('adminapp:admin_news_read'))
        else:
            pass
    else:
        news = BookNew.get_by_guid(news_id)
        form = BoorCreateUpdateForm(data=news)
    context = {
        'form': form,
        'news': news,
    }
    return render(request, 'adminapp/admin_news_update_delete.html', context)


@user_passes_test(lambda u: u.is_superuser)
def admin_news_delete(request, news_id):
    NewsNew.delete(news_id)
    return HttpResponseRedirect(reverse('adminapp:admin_new_read'))


@user_passes_test(lambda u: u.is_superuser)
def admin_comment_read(request):
    pass


@user_passes_test(lambda u: u.is_superuser)
def admin_basket_read(request):
    pass


@user_passes_test(lambda u: u.is_superuser)
def admin_order_read(request):
    pass

