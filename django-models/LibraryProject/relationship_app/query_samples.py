import os
import django

# Setup Django environment for standalone script
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "LibraryProject.settings")  # update if your settings path differs
django.setup()

from relationship_app.models import Author, Book, Library, Librarian

def books_by_author(author_name):
    try:
        author = Author.objects.get(name=author_name)
        books = Book.objects.filter(author=author)
        print(f"Books by {author_name}:")
        for book in books:
            print(f"- {book.title}")
    except Author.DoesNotExist:
        print(f"No author found with name '{author_name}'.")

def list_all_books():
    books = Book.objects.all()
    print("All books in the library system:")
    for book in books:
        print(f"- {book.title}")

def librarian_for_library(library_name):
    try:
        library = Library.objects.get(name=library_name)
        librarian = Librarian.objects.get(library=library)
        print(f"Librarian for {library_name}: {librarian.name}")
    except Library.DoesNotExist:
        print(f"No library found with name '{library_name}'.")
    except Librarian.DoesNotExist:
        print(f"No librarian assigned to library '{library_name}'.")

if __name__ == "__main__":
    # Examples - change these to match your data
    books_by_author("Jane Austen")
    print()
    list_all_books()
    print()
    librarian_for_library("Central Library")
