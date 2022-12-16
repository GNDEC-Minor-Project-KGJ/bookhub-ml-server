from django.db import models

# Create your models here.


class Book(models.Model):
    desc = models.TextField(blank=True, null=True)
    author = models.CharField(max_length=100, blank=True, null=True)
    genre = models.CharField(max_length=100, blank=True, null=True)
    url = models.URLField(blank=True, default="https://www.iconspng.com/images/book-generic-standing/book-generic-standing.jpg", null=True)
    rating = models.DecimalField(max_digits=4, decimal_places=2)
    title = models.CharField(max_length=300, blank=True, null=True)
    word_count = models.IntegerField(blank=True, default=-1, null=True)
    cleaned_desc = models.TextField(blank=True, default="", null=True)

    def __str__(self):
        return self.title
