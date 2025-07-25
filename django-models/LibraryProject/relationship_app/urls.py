from django.urls import path
from . import views
from .views import list_books

urlpatterns = [
    # Function based view - Lists all books
    # Urlpattern - /books/
    # view
    path('books/', views.list_books, name='list_books'),
    path('library/<int:pk>/', views.LibraryDetailView.as_view(), name='library_detail')
]
