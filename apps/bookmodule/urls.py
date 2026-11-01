from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="books.index"),
    path("list_books/", views.list_books, name="books.list_books"),
    path("<int:bookId>/", views.viewbook, name="books.view_one_book"),
    path("aboutus/", views.aboutus, name="books.aboutus"),
    path("html5/links/", views.links_view, name="books.html5_links"),
    path("html5/text/formatting/", views.text_formatting_view, name="books.html5_formatting"),
    path("html5/listing/", views.listing_view, name="books.html5_listing"),
    path("html5/tables/", views.tables_view, name="books.html5_tables"),
    path("search/", views.search_view, name="books.search"),  # Lab 6
    path("simple/query", views.simple_query, name="simple_query"),  # Lab 7
    path("complex/query", views.complex_query, name="complex_query"),  # Lab 7
]