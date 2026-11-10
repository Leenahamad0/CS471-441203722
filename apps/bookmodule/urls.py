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
    path("lab9/task1", views.lab9_task1, name="lab9_task1"),  # Lab 9 - Task 1
    path("lab9/task2", views.lab9_task2, name="lab9_task2"),  # Lab 9 - Task 2
    path("lab9/task3", views.lab9_task3, name="lab9_task3"),  # Lab 9 - Task 3
    path("lab9/task4", views.lab9_task4, name="lab9_task4"),  # Lab 9 - Task 4
    path("lab9/task5", views.lab9_task5, name="lab9_task5"),  # Lab 9 - Task 5
    path("lab9/task6", views.lab9_task6, name="lab9_task6"),  # Lab 9 - Task 6
    path("lab10_part1/listbooks", views.lab10_part1_list_books, name="lab10_part1_list"),  # Lab 10 - Part 1 - Task 1
    path("lab10_part1/addbook", views.lab10_part1_add_book, name="lab10_part1_add"),  # Lab 10 - Part 1 - Task 2
    path("lab10_part1/editbook/<int:book_id>", views.lab10_part1_edit_book, name="lab10_part1_edit"),  # Lab 10 - Part 1 - Task 3
    path("lab10_part1/deletebook/<int:book_id>", views.lab10_part1_delete_book, name="lab10_part1_delete"),  # Lab 10 - Part 1 - Task 4
    path("lab10_part2/listbooks", views.lab10_part2_list_books, name="lab10_part2_list"),  # Lab 10 - Part 2
    path("lab10_part2/addbook", views.lab10_part2_add_book, name="lab10_part2_add"),  # Lab 10 - Part 2
    path("lab10_part2/editbook/<int:book_id>", views.lab10_part2_edit_book, name="lab10_part2_edit"),  # Lab 10 - Part 2
    path("lab10_part2/deletebook/<int:book_id>", views.lab10_part2_delete_book, name="lab10_part2_delete"),  # Lab 10 - Part 2
]