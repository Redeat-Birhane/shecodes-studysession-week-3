from django.shortcuts import render # type: ignore
from datetime import date  # Import date for correct date handling
from .models import Author, Book

def create_authors_and_books(request):
    # Create authors
    author1, _ = Author.objects.get_or_create(name="Author One", birth_date=date(1980, 5, 12))
    author2, _ = Author.objects.get_or_create(name="Author Two", birth_date=date(1990, 8, 24))

    # Add books
    Book.objects.get_or_create(title="Book One", author=author1, published_date=date(2020, 1, 1), price=19.99)
    Book.objects.get_or_create(title="Book Two", author=author1, published_date=date(2021, 2, 20), price=25.99)
    Book.objects.get_or_create(title="Book Three", author=author2, published_date=date(2022, 3, 15), price=15.99)

    # Query books by author
    books_by_author1 = Book.objects.filter(author=author1)

    # Update book price
    book1 = Book.objects.get(title="Book One")
    book1.price = 18.99
    book1.save()

    # Delete a book
    Book.objects.filter(title="Book Three").delete()

    return render(request, 'books/book_list.html', {'books': books_by_author1})
