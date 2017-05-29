from django.conf.urls import url
from . import views

app_name = 'mylibrary'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^create_book/$', views.create_book, name='create_book'),
    url(r'^(?P<book_id>[0-9]+)/detail/$', views.detail, name='detail'),
    url(r'^(?P<book_id>[0-9]+)/favorite_book/$', views.favorite_book, name='favorite_book'),
    url(r'^(?P<book_id>[0-9]+)/delete_book/$', views.delete_book, name='delete_book'),
]