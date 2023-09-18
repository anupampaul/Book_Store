from django import forms 
from . import models

class BookStoreForm(forms.ModelForm): 
    class Meta:
        model = models.BookStore
        fields = ['id','name','author','category']