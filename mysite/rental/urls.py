from django.urls import path
from .views import (
    BooksView,
    FilmsView,
    CDsView,
    updateBook,
    updateCD,
    updateFilm,
    deleteBook,
    deleteFilm,
    deleteCD,
    addBook,
    addfilm,
    addcd,
    RentalsView,
    addRentals,
    updateRentals,
    deleteRentals,
    formStat,
    statchoice
)
from . import views


app_name = 'rental'
urlpatterns = [
    path('', BooksView.as_view(), name='index'),
    path('filmIndex', FilmsView.as_view(), name='filmIndex'),
    path('cdIndex', CDsView.as_view(), name='cdIndex'),
    path('rentals', RentalsView.as_view(), name='rentals'),
    path('formStat', formStat.as_view(), name='formStat'),
    path('statchoice', statchoice, name='statchoice'),
    path('addBook',addBook.as_view(), name='addbook'),
    path('addfilm',addfilm.as_view(), name='addfilm'),
    path('addcd',addcd.as_view(), name='addcd'),
    path('addrentals',addRentals.as_view(), name='addrentals'),
    path('book/<slug:slug>/update', updateBook.as_view(), name='update_book'),
    path('film/<slug:slug>/update', updateFilm.as_view(), name='update_film'),
    path('cd/<slug:slug>/update', updateCD.as_view(), name='update_cd'),
    path('rent/<slug:slug>/update', updateRentals.as_view(), name='update_rent'),
    path('book/<slug:slug>/delete', deleteBook.as_view(), name='delete_book'),
    path('film/<slug:slug>/delete', deleteFilm.as_view(), name='delete_film'),
    path('cd/<slug:slug>/delete', deleteCD.as_view(), name='delete_cd'),
    path('rent/<slug:slug>/delete', deleteRentals.as_view(), name='delete_rent'),
]

