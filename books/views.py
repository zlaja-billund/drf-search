from rest_framework import filters
from rest_framework import generics
from rest_framework.pagination import PageNumberPagination

from .serializers import BookSerializer
from .models import Book


# Create your views here.
class BookListView(generics.ListAPIView):
    serializer_class = BookSerializer
    model = Book
    queryset = Book.objects.all()
    filter_backends = [filters.SearchFilter]
    search_fields = ['genre', 'title']
