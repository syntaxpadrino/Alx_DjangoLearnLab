from bookshelf.models import Book
***

### `delete.md`



**Python command:**
```python
book = Book.objects.get(title="Nineteen Eighty-Four")
book.delete()
Book.objects.all()