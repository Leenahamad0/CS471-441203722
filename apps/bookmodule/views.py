from django.shortcuts import render, redirect, get_object_or_404  # Lab 10
from django.utils import timezone  # Lab 10
from django.db.models import Q  # Lab 8
from django.db.models import Count, Sum, Avg, Max, Min  # Lab 8 - Task 5
from .models import Book  # Lab 7
from .models import Student, Address  # Lab 8 - Task 7
from .models import Publisher  # Lab 9
from .models import Student2  # Lab 11 - Task 2
from .models import StudentCard  # Lab 11 - Task 3
from .forms import BookForm  # Lab 10 - Part 2
from .forms import StudentForm  # Lab 11
from .forms import Student2Form  # Lab 11 - Task 2
from .forms import StudentCardForm  # Lab 11 - Task 3


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


def lab10_part1_list_books(request):  # Lab 10 - Part 1 - Task 1
    books = Book.objects.all()
    return render(request, 'bookmodule/list_books.html', {'books': books})


def lab10_part1_add_book(request):  # Lab 10 - Part 1 - Task 2
    if request.method == 'POST':
        title = request.POST.get('title')
        price = request.POST.get('price')
        quantity = request.POST.get('quantity')
        # Create the book and automatically provide the current date/time for pubdate
        Book.objects.create(
            title=title,
            price=price,
            quantity=quantity,
            pubdate=timezone.now()
        )
        return redirect('lab10_part1_list')
    return render(request, 'bookmodule/add_book.html')


def lab10_part1_edit_book(request, book_id):  # Lab 10 - Part 1 - Task 3
    book = get_object_or_404(Book, id=book_id)
    if request.method == 'POST':
        book.title = request.POST.get('title')
        book.price = request.POST.get('price')
        book.quantity = request.POST.get('quantity')
        book.save()
        return redirect('lab10_part1_list')
    return render(request, 'bookmodule/edit_book.html', {'book': book})


def lab10_part1_delete_book(request, book_id):  # Lab 10 - Part 1 - Task 4
    book = get_object_or_404(Book, id=book_id)
    book.delete()
    return redirect('lab10_part1_list')


def lab10_part2_list_books(request):  # Lab 10 - Part 2
    books = Book.objects.all()
    return render(request, 'bookmodule/lab10_list_books.html', {'books': books})


def lab10_part2_add_book(request):  # Lab 10 - Part 2
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            book = form.save(commit=False)
            book.pubdate = timezone.now()  # Ensure the required pubdate field is filled
            book.save()
            return redirect('lab10_part2_list')
    else:
        form = BookForm()
    return render(request, 'bookmodule/lab10_add_book.html', {'form': form})


def lab10_part2_edit_book(request, book_id):  # Lab 10 - Part 2
    book = get_object_or_404(Book, id=book_id)
    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('lab10_part2_list')
    else:
        form = BookForm(instance=book)
    return render(request, 'bookmodule/lab10_edit_book.html', {'form': form, 'book': book})


def lab10_part2_delete_book(request, book_id):  # Lab 10 - Part 2
    book = get_object_or_404(Book, id=book_id)
    book.delete()
    return redirect('lab10_part2_list')


def student_list(request):  # Lab 11 - Task 1
    students = Student.objects.all()
    return render(request, 'bookmodule/student_list.html', {'students': students})


def student_add(request):  # Lab 11 - Task 1
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('student_list')
    else:
        form = StudentForm()
    return render(request, 'bookmodule/student_add.html', {'form': form})


def student_edit(request, student_id):  # Lab 11 - Task 1
    student = get_object_or_404(Student, id=student_id)
    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('student_list')
    else:
        form = StudentForm(instance=student)
    return render(request, 'bookmodule/student_edit.html', {'form': form, 'student': student})


def student_delete(request, student_id):  # Lab 11 - Task 1
    student = get_object_or_404(Student, id=student_id)
    student.delete()
    return redirect('student_list')


def student2_list(request):  # Lab 11 - Task 2
    students = Student2.objects.all()
    return render(request, 'bookmodule/student2_list.html', {'students': students})


def student2_add(request):  # Lab 11 - Task 2
    if request.method == 'POST':
        form = Student2Form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('student2_list')
    else:
        form = Student2Form()
    return render(request, 'bookmodule/student2_add.html', {'form': form})


def student2_edit(request, student_id):  # Lab 11 - Task 2
    student = get_object_or_404(Student2, id=student_id)
    if request.method == 'POST':
        form = Student2Form(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('student2_list')
    else:
        form = Student2Form(instance=student)
    return render(request, 'bookmodule/student2_edit.html', {'form': form, 'student': student})


def student2_delete(request, student_id):  # Lab 11 - Task 2
    student = get_object_or_404(Student2, id=student_id)
    student.delete()
    return redirect('student2_list')


def card_list(request):  # Lab 11 - Task 3
    cards = StudentCard.objects.all()
    return render(request, 'bookmodule/card_list.html', {'cards': cards})


def card_add(request):  # Lab 11 - Task 3
    if request.method == 'POST':
        # request.FILES carries the uploaded image
        form = StudentCardForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('card_list')
    else:
        form = StudentCardForm()
    return render(request, 'bookmodule/card_add.html', {'form': form})


def card_edit(request, card_id):  # Lab 11 - Task 3
    card = get_object_or_404(StudentCard, id=card_id)
    if request.method == 'POST':
        form = StudentCardForm(request.POST, request.FILES, instance=card)
        if form.is_valid():
            form.save()
            return redirect('card_list')
    else:
        form = StudentCardForm(instance=card)
    return render(request, 'bookmodule/card_edit.html', {'form': form, 'card': card})


def card_delete(request, card_id):  # Lab 11 - Task 3
    card = get_object_or_404(StudentCard, id=card_id)
    card.photo.delete(save=False)  # Remove the image file from the media folder
    card.delete()
    return redirect('card_list')