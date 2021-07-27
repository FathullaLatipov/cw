from django.db import models

from list_book.models import BookModel


class HistoryModel(models.Model):
    title = models.ManyToManyField(BookModel, related_name='history_title')
    desc = models.ManyToManyField(BookModel, related_name='history_desc')
    image = models.ManyToManyField(BookModel, related_name='history_image' )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'history'
        verbose_name_plural = 'history'
