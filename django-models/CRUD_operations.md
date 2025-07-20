## 1. Create a Book

This command adds a new book to the database.

```python
from bookshelf.models import Book
Book.objects.create(title="1984", author="George Orwell", published_year=1949)
# Expected Output: <Book: Book object (1)>

book = Book.objects.get(title="1984")
print(f"ID: {book.id}, Title: {book.title}, Author: {book.author}, Year: {book.published_year}")
# Expected Output: ID: 1, Title: 1984, Author: George Orwell, Year: 1949

book = Book.objects.get(id=1)
book.title = "Nineteen Eighty-Four"
book.save()

# Verify the change
updated_book = Book.objects.get(id=1)
print(updated_book.title)
# Expected Output: Nineteen Eighty-Four

book = Book.objects.get(title="Nineteen Eighty-Four")
book.delete()

# Confirm deletion by trying to retrieve all books
Book.objects.all()
# Expected Output: <QuerySet []>