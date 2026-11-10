from django import forms
from .models import Book
from .models import Student, Address  # Lab 11
from .models import Student2  # Lab 11 - Task 2
from .models import StudentCard  # Lab 11 - Task 3


class BookForm(forms.ModelForm):  # Lab 10 - Part 2
    class Meta:
        model = Book
        fields = ['title', 'price', 'quantity']


class StudentForm(forms.ModelForm):  # Lab 11 - Task 1
    class Meta:
        model = Student
        fields = ['name', 'age', 'address']


class Student2Form(forms.ModelForm):  # Lab 11 - Task 2
    class Meta:
        model = Student2
        fields = ['name', 'age', 'addresses']
        widgets = {
            'addresses': forms.CheckboxSelectMultiple(),
        }


class StudentCardForm(forms.ModelForm):  # Lab 11 - Task 3
    class Meta:
        model = StudentCard
        fields = ['name', 'university_id', 'photo']