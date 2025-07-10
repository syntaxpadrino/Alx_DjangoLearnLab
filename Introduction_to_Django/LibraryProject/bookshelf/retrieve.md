***

### `retrieve.md`


**Python command:**
```python
book = Book.objects.get(title="1984")
print(f"ID: {book.id}, Title: {book.title}, Author: {book.author}, Year: {book.published_year}")