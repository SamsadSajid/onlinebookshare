from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, redirect, render, HttpResponseRedirect, HttpResponse
from django.db.models import Q
from .models import BookList
from .form import BookForm
from django.contrib.auth.decorators import login_required
from feeds.models import Feed
from django.core.urlresolvers import reverse
from django.utils.safestring import mark_safe
from django.utils.html import escape
from django.contrib.auth.models import User
from django.forms.models import inlineformset_factory
from django.core.exceptions import PermissionDenied

IMAGE_FILE_TYPES = ['png', 'jpg', 'jpeg']


@login_required
def create_book(request):
    if not request.user.is_authenticated():
        render(request, 'core/cover.html')
    else:
        form = BookForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            books = form.save(commit=False)
            books.user = request.user
            books.logo = request.FILES['logo']
            file_type = books.logo.url.split('.')[-1]
            file_type = file_type.lower()
            if file_type not in IMAGE_FILE_TYPES:
                context = {
                    'books': books,
                    'form': form,
                    'error_message': 'Image file must be PNG, JPG, or JPEG',
                }
                return render(request, 'mylibrary/create_book.html', context)
            books.save()
            user = request.user
            welcome_post = '{0} has added <a href="{1}">{2}</a>.'.format(
                escape(user.username), reverse('mylibrary:index'), books.book_title)
            feed = Feed(user=user, post=welcome_post)
            feed.save()
            return render(request, 'mylibrary/detail.html', {'books': books})
        context = {
            "form": form,
        }
        return render(request, 'mylibrary/create_book.html', context)


def delete_book(request, book_id):
    book = BookList.objects.get(pk=book_id)
    book.delete()
    books = BookList.objects.filter(user=request.user)
    return render(request, 'mylibrary/index.html', {'books': books})


def favorite_book(request, book_id):
    book = get_object_or_404(BookList, pk=book_id)
    try:
        if book.isFavorite:
            book.isFavorite = False
        else:
            book.isFavorite = True
        book.save()
    except (KeyError, BookList.DoesNotExist):
        return JsonResponse({'success': False})
    else:
        return JsonResponse({'success': True}) #change here


@login_required
def detail(request, book_id):
    if not request.user.is_authenticated():
        render(request, 'core/cover.html')
    else:
        user = request.user
        books = get_object_or_404(BookList, pk=book_id)
        return render(request, 'mylibrary/detail.html', {'books': books, 'user': user})


def index(request):
    if not request.user.is_authenticated():
        render(request, 'core/cover.html')
    else:
        books = BookList.objects.filter(user=request.user)
        return render(request, 'mylibrary/index.html', {'books': books})





