from __future__ import unicode_literals
from django.contrib.auth.models import Permission, User
from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _
from django.db.models.signals import post_save


class BookList(models.Model):
    user = models.ForeignKey(User, default=1)
    #book = models.ForeignKey(on_delete=models.CASCADE)
    book_title = models.CharField(max_length=250)
    author = models.CharField(max_length=100)
    catagory = models.CharField(max_length=100)
    logo = models.FileField(upload_to='media/')
    isFavorite = models.BooleanField(default=False)
    owner = models.CharField(max_length=100)

    def __str__(self):
        return self.book_title



