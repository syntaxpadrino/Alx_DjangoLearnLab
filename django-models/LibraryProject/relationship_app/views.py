from django.shortcuts import render
from django.shortcuts import login, redirect
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

    return HttpResponse(books_text, content_type = "text/plain")

class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/list_books.html', 'relationship_app/library_detail.html'
    context_object_name = 'library'

    def get_context_date(self, **kwargs):
        context = super().get_context_data(**kwargs)

        library = self.get_object()
        context['books'] = library.books.all()

        return context

def register(request):
    # Handle user registration
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            # Create the user
            user = form.save()
            # Log user automatically
            login(request, user)
            return redirect('/')
    else:
        # Show empty form
        form = UserCreationForm()

    return render(request, 'registration/register.html', {'form':form})

@login_required
def profile(request):
    # Only logged-in users can see this
    return render(request, 'profile.html')
