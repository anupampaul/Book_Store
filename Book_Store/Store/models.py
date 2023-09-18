from django.db import models


# Create your models here.

class BookStore(models.Model):
    CATEGORY =(
        ('Mystery', 'Mystery'),
        ('Fiction', 'Fiction'),
        ('Thriller', 'Thriller'),
        ('Sci-Fi', 'Sci-Fi'),
        ('Horror', 'Horror'),
        ('Novel', 'Novel'),
    )
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=30)
    author = models.CharField(max_length=30)
    category = models.CharField(max_length=30, choices=CATEGORY)
    first_pub = models.DateTimeField(auto_now_add=True)
    last_pub = models.DateTimeField(auto_now=True)
