from django.urls import path

from book_history.views import HistoryListView

app_name = 'history'

urlpatterns = [
    path('', HistoryListView.as_view(), name="history")
]