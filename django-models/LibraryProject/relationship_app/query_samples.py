from relationship_app.models import Author, Book, Library, Librarian

def get_books_by_author(author_id):
    try:
        author = Author.objects.get(id=author_id)
        books = Book.objects.filter(author=author)
        print(f"Books by {author.name}:")
        for book in books:
            print(f"- {book.title} ({book.publication_year})")
        return books
    except Author.DoesNotExist:
        print("Author not found")
        return None

def list_all_books_in_library(library_id):
    try:
        library = Library.objects.get(id=library_id)
        books = library.books.all()
        print(f"Books in library '{library.name}':")
        for book in books:
            print(f"- {book.title} by {book.author.name} ({book.publication_year})")
        return books
    except Library.DoesNotExist:
        print("Library not found")
        return None

def get_librarian_for_library(library_id):
    try:
        library = Library.objects.get(id=library_id)
        librarian = Librarian.objects.get(library=library)
        print(f"Librarian for '{library.name}' is {librarian.name}")
        return librarian
    except Library.DoesNotExist:
        print("Library not found")
        return None
    except Librarian.DoesNotExist:
        print(f"No librarian assigned to '{library.name}'")
        return None

# Example usage
if __name__ == "__main__":
    get_books_by_author(1)
    list_all_books_in_library(1)
    get_librarian_for_library(1)
