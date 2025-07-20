from django.shortcuts import render
from django.http import HttpResponse
from .models import Book
from .models import Library


def list_books(request):

    books = Book.objects.all()

    book_list = []
    for book in books:
        book_list.append(f"{book.title} by {book.author.name}")

    books_text = "\n".join(book_list) if book_list else "No books available in the database."

    return HttpResponse(books_text, content_type = "text/plain")

class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'

    def get_context_date(self, **kwargs):
        context = super().get_context_data(**kwargs)

        library = self.get_object()
        context['books'] = library.books.all()

        return context
