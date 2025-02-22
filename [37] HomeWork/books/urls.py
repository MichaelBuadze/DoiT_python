from django.urls import path
from . import views

urlpatterns = [
    path('', views.list_books, name='list_books'),
    path('books/', views.list_books, name='list_books'),
    path('books/create/', views.create_book, name='create_book'),
    path('books/<int:book_id>/', views.book_detail, name='book_detail'),
    path('books/<int:book_id>/edit/', views.update_book, name='update_book'),
    path('books/<int:book_id>/delete/', views.delete_book, name='delete_book'),
]
