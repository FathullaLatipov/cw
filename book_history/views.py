from django.shortcuts import render
from django.views.generic import ListView

from book_history.models import HistoryModel


class HistoryListView(ListView):
    template_name = 'history.html'
    queryset = HistoryModel.objects.order_by('-pk')
