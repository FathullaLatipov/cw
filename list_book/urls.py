from django.urls import path

from list_book.views import BookListView

app_name = 'books'

urlpatterns = [
    path('', BookListView.as_view(), name="book")
]