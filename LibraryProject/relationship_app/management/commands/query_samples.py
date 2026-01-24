from django.core.management.base import BaseCommand
from relationship_app.models import Author, Book, Library, Librarian

class Command(BaseCommand):
    help = "Run sample queries for relationship_app"

    def handle(self, *args, **kwargs):
        # Clear previous data (optional)
        Author.objects.all().delete()
        Book.objects.all().delete()
        Library.objects.all().delete()
        Librarian.objects.all().delete()

        # Create sample data
        author = Author.objects.create(name="J.K. Rowling")
        book = Book.objects.create(title="Harry Potter and the Philosopher's Stone", author=author)
        library = Library.objects.create(name="Central Library")
        library.books.add(book)
        librarian = Librarian.objects.create(name="Alice", library=library)

        # Print queries
        self.stdout.write(f"Books by author: {list(author.books.all())}")
        self.stdout.write(f"Books in library: {list(library.books.all())}")
        self.stdout.write(f"Librarian of library: {library.librarian}")
