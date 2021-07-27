from django.urls import path

from book_history.views import HistoryDetailView

app_name = 'history'

urlpatterns = [
    path('<int:pk>/', HistoryDetailView.as_view(), name="history")
]
