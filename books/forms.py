from django import forms
from .models import Author, Book, Coment

class AuthorCreateForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ['first_name', 'last_name', 'email', 'bio']
        
class BookCreateForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['author', 'title', 'discribtion', 'cover_pic', 'isbn',]
        
        
        
class BookCommentForm(forms.ModelForm):
    class Meta:
        model = Coment
        fields = ['comment', 'star_given']