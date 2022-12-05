from django.db import models

# Create your models here.


class Book(models.Model):
    desc = models.TextField(blank=False, null=False)
    author = models.CharField(max_length=100, blank=False, null=False)
    genre = models.CharField(max_length=100, blank=False, null=False)
    url = models.URLField(blank=False, null=False)
    rating = models.DecimalField(max_digits=4, decimal_places=2)
    title = models.CharField(max_length=300, blank=False, null=False)
    word_count = models.IntegerField(blank=False, null=False)
    cleaned_desc = models.TextField(blank=False, null=False)

    def __str__(self):
        return self.title
