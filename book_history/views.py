from django.shortcuts import render
from django.views.generic import DetailView

from book_history.models import HistoryModel


class HistoryDetailView(DetailView):
    template_name = 'history.html'
    queryset = HistoryModel.objects.order_by('-pk')
