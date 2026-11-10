from django import forms
from .models import Book


class BookForm(forms.ModelForm):  # Lab 10 - Part 2
    class Meta:
        model = Book
        fields = ['title', 'price', 'quantity']