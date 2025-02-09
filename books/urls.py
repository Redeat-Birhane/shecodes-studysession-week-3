from django.urls import path # type: ignore
from . import views

urlpatterns = [
    path('create-books/', views.create_authors_and_books, name='create_books'),
]
