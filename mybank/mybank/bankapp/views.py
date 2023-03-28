from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from .models import Blog


def index(request):
    obj = Blog.objects.all()
    return render(request, 'index.html', {'obj': obj})


def registration(request):
    if request.method == 'POST':
        username = request.POST['username']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        password = request.POST['password']
        cpassword = request.POST['password1']
        if password == cpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request, "Username already exists")
                return redirect('/registration')
            elif User.objects.filter(email=email).exists():
                messages.info(request, "Email already exists")
                return redirect('/registration')
            else:
                user = User.objects.create_user(username=username, first_name=first_name, last_name=last_name,
                                                email=email, password=password)
                user.save();
                return redirect('/login')
        else:
            messages.info(request, "Password not matching")
            return redirect('/registration')
        return redirect('/login')
    return render(request, 'registration.html')


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('/new_page')
        else:
            messages.info(request, 'Invalid credentials')
            return redirect('/login')
    return render(request, 'login.html')


def new_page(request):
    return render(request, 'new_page.html')


def form(request):
    return render(request, 'form.html')


def submit(request):
    return render(request, 'submit.html')


def logout(request):
    auth.logout(request)
    return redirect('/')
