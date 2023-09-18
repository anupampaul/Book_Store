from django.shortcuts import render,redirect
from Store.forms import BookStoreForm
from Store.models import BookStore

# Create your views here.

def home(request):
    return render(request,'home.html')


def store_book(request):
    if request.method == 'POST':
        book = BookStoreForm(request.POST)
        if book.is_valid():
            book.save(commit=True)
            return redirect ('show_book')
    else:
        book = BookStoreForm()
    return render(request,'store_book.html', {'form':book})

def show_book(request):
    book = BookStore.objects.all()
    return render(request,'show_book.html', {'form':book})

def edit_book(request,id):
    book = BookStore.objects.get(pk = id)
    form = BookStoreForm(instance=book)
    if request.method == 'POST':
        form = BookStoreForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect ('show_book')
    return render(request,'store_book.html', {'form':form})

def delete_book(request,id):
    book = BookStore.objects.get(pk = id).delete()
    return redirect ('show_book')