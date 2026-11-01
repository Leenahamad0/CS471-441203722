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
    path("lab8/task1", views.lab8_task1, name="lab8_task1"),  # Lab 8
    path("lab8/task2", views.lab8_task2, name="lab8_task2"),  # Lab 8
    path("lab8/task3", views.lab8_task3, name="lab8_task3"),  # Lab 8
    path("lab8/task4", views.lab8_task4, name="lab8_task4"),  # Lab 8
    path("lab8/task5", views.lab8_task5, name="lab8_task5"),  # Lab 8
    path("lab8/task7", views.student_city_count, name="student_city_count"),  # Lab 8
]