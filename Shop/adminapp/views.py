import os

from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import user_passes_test
from django.urls import reverse

from authapp.models import User
from database import BookNew
from mainapp.forms import BoorCreateUpdateForm, ImagesForBookForm
from mainapp.models import ImageBook


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
def admin_qoute_read(request):
    pass


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
