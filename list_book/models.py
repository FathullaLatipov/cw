from django.db import models


class BookModel(models.Model):
    title = models.CharField(max_length=40)
    description = models.TextField()
    image = models.FileField(upload_to='books')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'book'
        verbose_name_plural = 'books'



