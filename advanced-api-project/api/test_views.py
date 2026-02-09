from django.urls import reverse
from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.test import APITestCase

from api.models import Author, Book
class BookAPITestCase(APITestCase):

    def setUp(self):
        # Create a user
        self.user = User.objects.create_user(
            username="testuser",
            password="testpass123"
        )

        # Create author
        self.author = Author.objects.create(name="George Orwell")

        # Create book
        self.book = Book.objects.create(
            title="1984",
            publication_year=1949,
            author=self.author
        )

        self.list_url = reverse('book-list')
        self.detail_url = reverse('book-detail', args=[self.book.id])
    def test_get_books_list(self):
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
    def test_get_single_book(self):
        response = self.client.get(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], "1984")
    def test_create_book_authenticated(self):
        self.client.login(username="testuser", password="testpass123")

        data = {
            "title": "Animal Farm",
            "publication_year": 1945,
            "author": self.author.id
        }

        response = self.client.post(self.list_url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    def test_create_book_unauthenticated(self):
        data = {
            "title": "Unauthorized Book",
            "publication_year": 2000,
            "author": self.author.id
        }

        response = self.client.post(self.list_url, data)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
    def test_update_book(self):
        self.client.login(username="testuser", password="testpass123")

        data = {
            "title": "1984 Updated",
            "publication_year": 1949,
            "author": self.author.id
        }

        response = self.client.put(self.detail_url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], "1984 Updated")
    def test_delete_book(self):
        self.client.login(username="testuser", password="testpass123")

        response = self.client.delete(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
    def test_filter_books_by_year(self):
        response = self.client.get(self.list_url + '?publication_year=1949')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    def test_search_books(self):
        response = self.client.get(self.list_url + '?search=1984')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    def test_order_books(self):
        response = self.client.get(self.list_url + '?ordering=title')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
