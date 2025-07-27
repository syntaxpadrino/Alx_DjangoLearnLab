from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Book
from .models import Library
from django.views.generic.detail import DetailView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required

def list_books(request):
    books = Book.objects.all()
    book_list = []
    for book in books:
        book_list.append(f"{book.title} by {book.author.name}")

    books_text = "\n".join(book_list) if book_list else "No books available in the database."
    return HttpResponse(books_text, content_type="text/plain")

class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        library = self.get_object()
        context['books'] = library.books.all()
        return context

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('list_books')  # Redirect to a valid URL name
    else:
        form = UserCreationForm()
    
    return render(request, 'relationship_app/register.html', {'form': form})

@login_required
def profile(request):
    return render(request, 'relationship_app/profile.html')