from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=64)


class Author(models.Model):
    first_name = models.CharField(max_length=128)
    last_name = models.CharField(max_length=128)
    birthday = models.DateField()


class Book(models.Model):
    name = models.CharField(max_length=512)
    publish_date = models.DateField(null=False, blank=False)
    author = models.ForeignKey(Author, on_delete=models.PROTECT, related_name="books")
    categories = models.ManyToManyField(Category, related_name="books")
