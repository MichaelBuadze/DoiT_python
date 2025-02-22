from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=100)
    authors = models.CharField(max_length=100)
    publication = models.CharField(max_length=15)
    isbn = models.CharField(max_length=11)


    def __str__(self):
        return self.title

# Create your models here.
