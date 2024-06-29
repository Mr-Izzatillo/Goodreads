from django.shortcuts import render, redirect
from django.views import View
from .forms import AuthorCreateForm, BookCreateForm, BookCommentForm
from .models import Author, Book, Coment
from django.urls import reverse
from django.contrib.auth.mixins import LoginRequiredMixin

class Author_create(View, LoginRequiredMixin):
    def get(self, request):
        author = Author.objects.all()
        context = {'aftors':author}
        return render(request, 'aftor.html', context=context)
    
    
class AuthorAddView(View, LoginRequiredMixin):
    def get(self, request):
        form = AuthorCreateForm()
        return render(request, 'author_add.html', context={'form':form})
    
    def post(self, request):
        form = AuthorCreateForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            return render(request, 'author_add.html', context={'form':form})



class Book_create(View, LoginRequiredMixin):
    def get(self, request):
        book = Book.objects.all()
        context = {'books':book}
        return render(request, 'kitob.html', context=context)
    
class BookAddView(View, LoginRequiredMixin):
    def get(self, request):
        form = BookCreateForm()
        return render(request, 'book_add.html', context={'form':form})
    
    def post(self, request):
        form = BookCreateForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            return redirect('books:kitob')
        else:
            return render(request, 'book_add.html', context={'form':form})
        
        
class BookDetail(View, LoginRequiredMixin):
    def get(self, request, id):
        book = Book.objects.get(id=id)
        form = BookCommentForm()
        context = {'book':book, 'form':form}
        return render(request, 'book_detail.html', context=context)
    
    
class BookCommentView(View, LoginRequiredMixin):
    def post(self, request, id):
        book  = Book.objects.get(id=id)
        form = BookCommentForm(data=request.POST, instance=book)
        if form.is_valid():
            Coment.objects.create(
                user=request.user,
                book=book,
                comment = form.cleaned_data.get('comment'),
                star_given = form.cleaned_data.get('star_given')
                
            )
            return redirect(reverse('books:detail', kwargs={'id': book.id}))
        return render(request, 'books:detail.html',{'book':book, 'form':form})

