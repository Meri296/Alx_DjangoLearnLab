from rest_framework import generics, permissions
from .models import Book
from .serializers import BookSerializer


# List all books (READ-ONLY, public)
class BookListView(generics.ListAPIView):
    """
    Retrieves a list of all books.
    Accessible to unauthenticated users (read-only).
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny]


# Retrieve a single book by ID (READ-ONLY, public)
class BookDetailView(generics.RetrieveAPIView):
    """
    Retrieves a single book by its ID.
    Accessible to unauthenticated users (read-only).
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny]


# Create a new book (AUTHENTICATED ONLY)
class BookCreateView(generics.CreateAPIView):
    """
    Creates a new book.
    Only authenticated users are allowed.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]


# Update an existing book (AUTHENTICATED ONLY)
class BookUpdateView(generics.UpdateAPIView):
    """
    Updates an existing book.
    Only authenticated users are allowed.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]


# Delete a book (AUTHENTICATED ONLY)
class BookDeleteView(generics.DestroyAPIView):
    """
    Deletes a book.
    Only authenticated users are allowed.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]
