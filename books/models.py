from django.db import models

# Create your models here.
class Book(models.Model):
    author_id = models.IntegerField(default=0)
    genre = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    publication_year = models.IntegerField(default=0000)
    isbn = models.CharField(max_length=255)
    page_count = models.IntegerField(default=0)
    rating = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)
    is_available = models.BooleanField(default=False)
    description = models.TextField(null=True, blank=True)


    def __str__(self):
        return self.title