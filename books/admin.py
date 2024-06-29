from django.contrib import admin
from .models import Book, Author, Coment

admin.site.register([Book, Author, Coment])
