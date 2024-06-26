from django.db import models

class Book(models.Model):
    name = models.CharField(max_length=100)
    page_count = models.IntegerField()
    category = models.CharField(max_length=50)
    author_name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='book_images/', null=True, blank=True)

    def __str__(self):
        return self.name
