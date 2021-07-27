from django.shortcuts import render
from django.urls import reverse
from django.views.generic import ListView
from list_book.models import BookModel


class BookListView(ListView):
    template_name = 'book.html'
    queryset = BookModel.objects.order_by('pk')

