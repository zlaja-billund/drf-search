from django.contrib import admin
from .models import Book

# Register your models here.
class BookAdmin(admin.ModelAdmin):
    exclude = []

admin.site.register(Book, BookAdmin)