from django import forms
from django.contrib.auth.models import User

from .models import BookList


class BookForm(forms.ModelForm):

    class Meta:
        model = BookList
        fields = ['book_title', 'author', 'catagory', 'logo', 'owner']

