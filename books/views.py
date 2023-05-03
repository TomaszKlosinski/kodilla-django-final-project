from django.http import HttpResponse
from django.shortcuts import render
from django.contrib import messages
from django.core.paginator import Paginator

from books.models import Book, Author


def books_list(request):
   books = Book.objects.all()

   paginator = Paginator(books, 3)
   page_number = request.GET.get('page')
   books = paginator.get_page(page_number)

   return render(
       request=request,
       template_name="books/books_list.html",
       context={"books": books}
   )


def book_details(request, id):
   book = Book.objects.get(id=id)
   return render(
       request=request,
       template_name="books/book_details.html",
       context={"book": book}
   )


def authors_list(request):
   authors = Author.objects.all()
   return render(
       request=request,
       template_name="books/authors_list.html",
       context={"authors": authors}
   )


def author_details(request, id):
   author = Author.objects.get(id=id)
   author_books = Book.objects.filter(author_id=author.id)
   return render(
       request=request,
       template_name="books/author_details.html",
       context={"author": author, "author_books": author_books}
   )
