from django.db import models
from django.db.models import Sum  # Lab 9


class Publisher(models.Model):  # Lab 9
    name = models.CharField(max_length=200)
    location = models.CharField(max_length=300)


class Author(models.Model):  # Lab 9
    name = models.CharField(max_length=200)
    DOB = models.DateField(null=True)


class Book(models.Model):  # Lab 9
    title = models.CharField(max_length=100)
    price = models.FloatField(default=0.0)
    quantity = models.IntegerField(default=1)
    pubdate = models.DateTimeField()
    rating = models.SmallIntegerField(default=1)
    publisher = models.ForeignKey(Publisher, null=True, on_delete=models.SET_NULL)
    authors = models.ManyToManyField(Author)

    def __str__(self):  # Lab 9 - Task 1
        return self.title

    @property
    def availability_percentage(self):
        # Calculate the total quantity across all books in the database
        total_quantity = Book.objects.aggregate(sum_qty=Sum('quantity'))['sum_qty']
        if total_quantity and total_quantity > 0:
            return round((self.quantity / total_quantity) * 100, 2)
        return 0


class Address(models.Model):  # Lab 8 - Task 6
    city = models.CharField(max_length=50)

    def __str__(self):
        return self.city


class Student(models.Model):  # Lab 8 - Task 6
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    address = models.ForeignKey(Address, on_delete=models.CASCADE)

    def __str__(self):
        return self.name