from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from .views import list_books

urlpatterns = [
    # Function based view - Lists all books
    # Urlpattern - /books/
    # view
    path('books/', views.list_books, name='list_books'),
    path('library/<int:pk>/', views.LibraryDetailView.as_view(), name='library_detail'),

    path('login/', auth_views.LoginView.as_view(template_name = 'registration/login.html'), name='login'),
    path('logout/', auth_views.LogOutView.as_view(template_name = "registration/logout.html"), name='logout'),
    path('register/', views.register, name = 'register'),
]
