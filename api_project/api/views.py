from rest_framework import generics, viewsets
from .models import Book
from .serializers import BookSerializer
from rest_framework import generics, viewsets, permissions



# Existing ListAPIView (keep this!)
class BookList(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


# NEW ViewSet for full CRUD
class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]


