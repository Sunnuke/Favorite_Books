from django.shortcuts import render, redirect, HttpResponse
from .models import *
from django.contrib import messages

# Create your views here.

def books(request):
    context = {
        'User': User.objects.get(id=request.session['user']),
        'Books': Book.objects.all()
    }
    return render(request, 'books.html', context)

def showBook(request, num):
    context = {
        'User': User.objects.get(id=request.session['user']),
        'Book': Book.objects.get(id=num)
    }
    return render(request, 'bookdetails.html', context)

def add(request):
    errors = Book.objects.valid_book(request.POST)
    if len(errors) > 0:
        print('There are', len(errors), 'ERRORS!!!')
        for key, val in errors.items():
            print(key, val)
            messages.error(request, val)
        return redirect('/books')
    else:
        print('No errors')
        Book.objects.create(
            title=request.POST['title'],
            desc=request.POST['desc'],
            uploaded_by=User.objects.get(id=request.session['user'])
        )
        num = Book.objects.last().id
        Book.objects.get(id=num).users_who_like.add(User.objects.get(id=request.session['user']))
        num = str(num)
    return redirect('/books')

def edit(request, num):
    errors = Book.objects.BookManager(request.POST)
    reNum = str(num)
    if len(errors) > 0:
        print('There are', len(errors), 'ERRORS!!!')
        for key, val in errors.items():
            print(key, val)
            messages.error(request, val)
        return redirect('/book/'+reNum)
    else:
        print('No errors')
        c = Book.objects.get(id=num)
        c.title=request.POST['title']
        c.desc=request.POST['desc']
        c.save()
        num = str(num)
    return redirect('/book/'+num)

def favorite(request):
    return redirect('/')

def unfavorite(request):
    return redirect('/')

def delete(request):
    return redirect('/')

