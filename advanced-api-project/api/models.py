from django.db import models

# Author model represents a writer who can have many books
class Author(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


# Book model represents a book written by one author
class Book(models.Model):
    title = models.CharField(max_length=200)
    publication_year = models.IntegerField()

    # One author can have many books (one-to-many relationship)
    author = models.ForeignKey(
        Author,
        related_name='books',
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.title
