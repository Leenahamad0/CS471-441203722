from django.shortcuts import render
from django.db.models import Q  # Lab 8
from django.db.models import Count, Sum, Avg, Max, Min  # Lab 8 - Task 5
from .models import Book  # Lab 7
from .models import Student, Address  # Lab 8 - Task 7
from .models import Publisher  # Lab 9


def index(request):
    return render(request, "bookmodule/index.html")


def list_books(request):
    return render(request, "bookmodule/list_books.html")


def viewbook(request, bookId):
    return render(request, "bookmodule/one_book.html")


def aboutus(request):
    return render(request, "bookmodule/aboutus.html")


def links_view(request):
    return render(request, "bookmodule/links.html")


def text_formatting_view(request):
    return render(request, "bookmodule/text_formatting.html")


def listing_view(request):
    return render(request, "bookmodule/listing.html")


def tables_view(request):
    return render(request, "bookmodule/tables.html")


def __getBooksList():  # Lab 6
    book1 = {'id': 12344321, 'title': 'Continuous Delivery', 'author': 'J.Humble and D. Farley'}
    book2 = {'id': 56788765, 'title': 'Reversing: Secrets of Reverse Engineering', 'author': 'E. Eilam'}
    book3 = {'id': 43211234, 'title': 'The Hundred-Page Machine Learning Book', 'author': 'Andriy Burkov'}
    return [book1, book2, book3]


def search_view(request):  # Lab 6
    if request.method == "POST":
        keyword = request.POST.get('keyword')
        string = keyword.lower() if keyword else ''
        isTitle = request.POST.get('option1')
        isAuthor = request.POST.get('option2')

        # Filter books
        books = __getBooksList()
        newBooks = []
        for item in books:
            contained = False
            if isTitle and string in item['title'].lower():
                contained = True
            if not contained and isAuthor and string in item['author'].lower():
                contained = True
            if contained:
                newBooks.append(item)

        return render(request, 'bookmodule/bookList.html', {'books': newBooks})

    return render(request, 'bookmodule/search.html')


def simple_query(request):  # Lab 7
    mybooks = Book.objects.filter(title__icontains='and')  # Filters books where title contains 'and'
    return render(request, 'bookmodule/bookList.html', {'books': mybooks})


def complex_query(request):  # Lab 7
    mybooks = Book.objects.filter(author__isnull=False).filter(title__icontains='and').filter(edition__gte=2).exclude(price__lte=100)[:10]
    if len(mybooks) >= 1:
        return render(request, 'bookmodule/bookList.html', {'books': mybooks})
    else:
        return render(request, 'bookmodule/index.html')


def lab8_task1(request):  # Lab 8 - Task 1
    books = Book.objects.filter(Q(price__lte=80))
    return render(request, 'bookmodule/bookList.html', {'books': books})


def lab8_task2(request):  # Lab 8 - Task 2
    books = Book.objects.filter(Q(edition__gt=3) & (Q(title__icontains='qu') | Q(author__icontains='qu')))
    return render(request, 'bookmodule/bookList.html', {'books': books})


def lab8_task3(request):  # Lab 8 - Task 3
    books = Book.objects.filter(~Q(edition__gt=3) & (~Q(title__icontains='qu') | ~Q(author__icontains='qu')))
    return render(request, 'bookmodule/bookList.html', {'books': books})


def lab8_task4(request):  # Lab 8 - Task 4
    books = Book.objects.all().order_by('title')
    return render(request, 'bookmodule/bookList.html', {'books': books})


def lab8_task5(request):  # Lab 8 - Task 5
    aggregations = Book.objects.aggregate(
        total_books=Count('id'),
        total_price=Sum('price'),
        average_price=Avg('price'),
        max_price=Max('price'),
        min_price=Min('price')
    )
    return render(request, 'bookmodule/bookStats.html', {'aggregations': aggregations})


def student_city_count(request):  # Lab 8 - Task 7
    # Annotate each City with the count of related students
    cities = Address.objects.annotate(student_count=Count('student'))
    return render(request, 'bookmodule/studentCityCount.html', {'cities': cities})


def lab9_task1(request):  # Lab 9 - Task 1
    books = Book.objects.all()
    return render(request, 'bookmodule/bookAvailability.html', {'books': books})


def lab9_task2(request):  # Lab 9 - Task 2
    # Annotate each publisher with the sum of book quantities
    publishers = Publisher.objects.annotate(total_stock=Sum('book__quantity'))
    return render(request, 'bookmodule/publisherStock.html', {'publishers': publishers})


def lab9_task3(request):  # Lab 9 - Task 3
    # Annotate each publisher with the minimum (oldest) book publication date
    publishers = Publisher.objects.annotate(oldest_pubdate=Min('book__pubdate'))
    return render(request, 'bookmodule/oldestBookPublisher.html', {'publishers': publishers})


def lab9_task4(request):  # Lab 9 - Task 4
    # Annotate each publisher with the average, min, and max price of their books
    publishers = Publisher.objects.annotate(
        avg_price=Avg('book__price'),
        min_price=Min('book__price'),
        max_price=Max('book__price')
    )
    return render(request, 'bookmodule/publisherPriceStats.html', {'publishers': publishers})


def lab9_task5(request):  # Lab 9 - Task 5
    # Annotate publishers with the count of books that have a high rating (rating >= 4)
    # and include their total quantity as well
    publishers = Publisher.objects.annotate(
        high_rated_count=Count('book', filter=Q(book__rating__gte=4)),
        total_quantity=Sum('book__quantity')
    )
    return render(request, 'bookmodule/highRatedBooks.html', {'publishers': publishers})


def lab9_task6(request):  # Lab 9 - Task 6
    # Count books for each publisher, only books with
    # price > 50 and 1 <= quantity < 5
    publishers = Publisher.objects.annotate(
        book_count=Count(
            'book',
            filter=Q(book__price__gt=50) & Q(book__quantity__lt=5) & Q(book__quantity__gte=1)
        )
    )
    return render(request, 'bookmodule/publisherFilteredCount.html', {'publishers': publishers})