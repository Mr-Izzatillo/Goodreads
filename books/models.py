from django.db import models
from users.models import User
from django.utils import timezone
from django.core.validators import MinValueValidator, MaxValueValidator

class Book(models.Model):
    author = models.ForeignKey('books.Author', on_delete=models.CASCADE, related_name='books')
    title = models.CharField(max_length=255)
    discribtion = models.TextField()
    isbn = models.CharField(max_length=20)
    cover_pic = models.ImageField(default='defoult_cover_pic.jpg', upload_to='books_image')
    
    def __str__(self) -> str:
        return self.title


class Author(models.Model):
    first_name = models.CharField(max_length=200)   
    last_name = models.CharField(max_length=200)
    email = models.EmailField()
    bio = models.TextField()
    
    def __str__(self) -> str:
        return self.first_name
    
    
class Coment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE,related_name='coments')
    comment = models.TextField()
    star_given = models.IntegerField(validators=(MaxValueValidator(1), MinValueValidator(5)))
    created_at = models.DateTimeField(default = timezone.now)