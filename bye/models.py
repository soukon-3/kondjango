from django.db import models

# Create your models here.
# hello/models.py

from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    published_date = models.DateField()
    isbn_number = models.CharField(max_length=13)
    pages = models.IntegerField()
    cover_image = models.URLField()
    language = models.CharField(max_length=2)
    genre = models.CharField(max_length=50, null=True)  # 新しいフィールドを追加
    
    def __str__(self):
        return self.title
