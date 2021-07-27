from django.contrib import admin

from list_book.models import BookModel


@admin.register(BookModel)
class BookModelAdmin(admin.ModelAdmin):
    list_display = ['title', 'description', 'created_at']
    list_filter = ['title', 'description', 'created_at']
    search_fields = ['title',]