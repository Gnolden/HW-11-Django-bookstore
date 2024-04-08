from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from .models import Book

def book_list(request):
    books = Book.objects.all()
    data = {'books': list(books.values())}
    return JsonResponse(data)

def book_detail(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    data = {'book': {
        'name': book.name,
        'page_count': book.page_count,
        'category': book.category,
        'author_name': book.author_name,
        'price': str(book.price),
        'image_url': book.image.url if book.image else None
    }}
    return JsonResponse(data)
