import django_tables2 as tables
from .models import Book

class BookTable(tables.Table):
    class Meta:
        model = Book
        attrs = {'class': 'paleblue'}