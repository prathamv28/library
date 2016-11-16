from django.shortcuts import render , redirect
from .forms import *
from .models import *
from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login , logout
from django.contrib.auth.decorators import login_required
from django_tables2 import RequestConfig
from .tables import BookTable
from django.core.exceptions import ObjectDoesNotExist

def index(request):
    logout(request)
    return render(request,'index.html')


def register1(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(
            username=form.cleaned_data['username'],
            password=form.cleaned_data['password'],
            email=form.cleaned_data['email']
            )
            user.first_name=form.cleaned_data['first_name']
            user.last_name=form.cleaned_data['last_name']
            user.save()
            librarian=Librarian(user.id)
            librarian.save()
            return render(request , 'registered.html')
    else:
        form = RegistrationForm()

    return render(request, 'register1.html', {'form': form})

def register2(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(
            username=form.cleaned_data['username'],
            password=form.cleaned_data['password'],
            email=form.cleaned_data['email']
            )
            user.first_name=form.cleaned_data['first_name']
            user.last_name=form.cleaned_data['last_name']
            user.save()
            customer=Customer(user.id)
            customer.save()
            return render(request , 'registered.html')
    else:
        form = RegistrationForm()

    return render(request, 'register2.html', {'form': form})


def login1(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password=form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                try:
                    user.librarian
                except:
                    return render(request , 'login_fail1.html' , {'form':form})

                login(request, user)
                return redirect('/librarian',{'message':"Hello , " + request.user.first_name})

            else:
                form = LoginForm()
                return render(request , 'login_fail1.html' , {'form':form})
    else:
        form = LoginForm()

    return render(request, 'login1.html', {'form': form})

def login2(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password=form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                try:
                    user.customer
                except:
                    return render(request , 'login_fail2.html' , {'form':form})

                login(request, user)
                return redirect('/customer',{'message':"Hello , " + request.user.first_name})

            else:
                form = LoginForm()
                return render(request , 'login_fail2.html' , {'form':form})
    else:
        form = LoginForm()

    return render(request, 'login2.html', {'form': form})


@login_required
def add_book(request):
    try:
        request.user.librarian
    except:
        return redirect('/')
    if request.method == 'POST':
        form = AddBookForm(request.POST)
        if form.is_valid():
                title=form.cleaned_data['title']
                count=form.cleaned_data['count']
                author=form.cleaned_data['author']
                all_books=Book.objects.all()
                for book in all_books:
                    if book.title.lower() == title.lower() and book.author.lower()==author.lower():
                        book.count=book.count + count
                        book.save()
                        return redirect('/librarian')
                publisher=form.cleaned_data['publisher']
                book=Book()
                book.title=title
                book.author=author
                book.publisher=publisher
                book.count=count
                book.save()
                return redirect('/librarian')
    else:
        form = AddBookForm()

    return render(request, 'add_book.html', {'form': form})


@login_required
def librarian(request):
    try:
        request.user.librarian
    except:
        return redirect('/')
    message=""
    if request.method=='POST':
        bid = request.POST['bid']
        try:
            book=Book.objects.get(id=bid)
        except Book.DoesNotExist:
            book=None
        if book:
            if request.POST['action']=="edit":
                form = EditBookForm(initial={'title': book.title, 'author': book.author,'publisher':book.publisher, 'count':book.count,'bid':bid})
                return render(request,'edit_book.html', {'form':form})
            else:
                if book.issued_count==0:
                    book.delete()
                message="Book deleted"
                table = BookTable(Book.objects.all())
                RequestConfig(request , paginate={'per_page': 20}).configure(table)
                greeting="Hello , " + request.user.first_name
        else:
            message="Invalid Book ID"
            table = BookTable(Book.objects.all())
            RequestConfig(request , paginate={'per_page': 20}).configure(table)
            greeting="Hello , " + request.user.first_name

    else:
        table = BookTable(Book.objects.all())
        RequestConfig(request , paginate={'per_page': 20}).configure(table)
        greeting="Hello , " + request.user.first_name

    return render(request , 'librarian.html' , {'table':table,'message':message,'greeting':greeting})


@login_required
def edit(request):
    try:
        request.user.librarian
    except:
        return redirect('/')
    bid=request.POST['bid']
    book=Book.objects.get(id=bid)
    book.title=request.POST['title']
    book.author=request.POST['author']
    book.publisher=request.POST['publisher']
    book.count=request.POST['count']
    book.save()
    return redirect('/librarian')


@login_required
def customer(request):
    try:
        customer=request.user.customer
    except:
        return redirect('/')
    try:
        issued=customer.issued_book
    except ObjectDoesNotExist:
        issued=None
    message=""
    if request.method == 'POST':
        if not issued:
            try:
                book=Book.objects.get(id=request.POST['bid'])
            except Book.DoesNotExist:
                book=None
            if book:
                if book.count-book.issued_count>0:
                    customer.issued_book=book
                    issued=book
                    customer.save()
                    book.count=book.count - 1
                    book.issued_count+=1
                    book.save()
                else:
                    message="This book isn't available right now"
            else:
                message="Invalid Book ID"
        else:
            message="You already have a book issued"
        table = BookTable(Book.objects.all())
        RequestConfig(request , paginate={'per_page': 20}).configure(table)
        greeting="Hello , " + request.user.first_name

    else:
        table = BookTable(Book.objects.all())
        RequestConfig(request , paginate={'per_page': 20}).configure(table)
        greeting="Hello , " + request.user.first_name
    return render(request , 'customer.html' , {'table':table,'greeting':greeting , 'issued':issued ,'message':message})


@login_required
def return_book(request):
    try:
        customer=request.user.customer
    except:
        return redirect('/')
    book_issued=customer.issued_book
    customer.issued_book=None
    customer.save()
    book_issued.issued_count-=1
    book_issued.save()
    return redirect('/customer')