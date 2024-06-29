from django.urls import path
from .views import Author_create, Book_create, BookAddView, AuthorAddView, BookDetail, BookCommentView
app_name = 'books'

urlpatterns = [
    path('aftor/', Author_create.as_view(), name='aftor'),
    path('', Book_create.as_view(), name='kitob'),
    path('add/', BookAddView.as_view(), name='book_add'),
    path('authoradd/', AuthorAddView.as_view(), name='authoradd'),
    path('<int:id>/', BookDetail.as_view(), name='detail'),
    path('<int:id>/comment/', BookCommentView.as_view(), name='book_comment')
]
