from django.core.management.base import BaseCommand # type: ignore
from books.models import Author, Book

class Command(BaseCommand):
    help = 'Create authors and books'

    def handle(self, *args, **kwargs):
        author1, _ = Author.objects.get_or_create(name="Author One", birth_date="1980-05-12")
        author2, _ = Author.objects.get_or_create(name="Author Two", birth_date="1990-08-24")

        Book.objects.get_or_create(title="Book One", author=author1, published_date="2020-01-01", price=19.99)
        Book.objects.get_or_create(title="Book Two", author=author1, published_date="2021-02-20", price=25.99)
        Book.objects.get_or_create(title="Book Three", author=author2, published_date="2022-03-15", price=15.99)

        self.stdout.write(self.style.SUCCESS('Successfully created authors and books'))
