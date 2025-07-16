# Alx_DjangoLearnLab/django-models/relationship_app/query_samples.py

import os
import django

# Set up the Django environment to allow standalone script usage
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings')
django.setup()

# Import the models from your app
from .models import Author, Book, Library, Librarian

def run_sample_queries():
    """
    Executes and prints the results of several sample queries
    to demonstrate Django ORM relationships.
    """
    print("--- Running Sample Queries ---")

    # Query 1: Get all books by a specific author.
    # We'll get the first author from the database for this example.
    print("\n## 1. Querying all books by a specific author:")
    author = Author.objects.first()
    if author:
        # Use the reverse relationship ('book_set') or filter directly
        books_by_author = Book.objects.filter(author=author)
        print(f"Found books for author: {author.name}")
        for book in books_by_author:
            print(f"  - {book.title}")
    else:
        print("No authors found in the database to query.")

    # -----------------------------------------------------------------

    # Query 2: List all books in a specific library.
    # We'll get the first library from the database for this example.
    print("\n## 2. Listing all books in a library:")
    library = Library.objects.first()
    if library:
        # Access the ManyToManyField directly to get all related books
        books_in_library = library.book.all()
        print(f"Found books in library: {library.name}")
        for book in books_in_library:
            print(f"  - {book.title}")
    else:
        print("No libraries found in the database to query.")

    # -----------------------------------------------------------------

    # Query 3: Retrieve the librarian for a library.
    # We'll get the first library that has a librarian assigned.
    print("\n## 3. Retrieving the librarian for a library:")
    library_with_librarian = Library.objects.filter(librarian__isnull=False).first()
    if library_with_librarian:
        # Access the OneToOneField directly
        librarian = library_with_librarian.librarian
        print(f"The librarian for '{library_with_librarian.name}' is {librarian.name}.")
    else:
        print("No libraries with an assigned librarian found.")

    print("\n--- Queries Finished ---")


# Make the script executable
if __name__ == "__main__":
    run_sample_queries()