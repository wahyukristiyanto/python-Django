from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm # Signup & Signin Form
from django.contrib.auth.models import User # to Make User
from django.db import IntegrityError # so the username is unique
from django.contrib.auth import login, logout, authenticate # for login & logout
from .forms import TodoForm # import forms.py
from .models import Todo # import Todo Model to get the data of Todo

def home(request):
    return render(request, 'todo/home.html')

# Create your views here.
def signupuser(request):
    if request.method == 'GET':
        # Sign Up Form from Django
        return render(request, 'todo/signupuser.html', {'form':UserCreationForm()})
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(request.POST['username'], password=request.POST['password1'])
                user.save() # save user
                login(request, user) # login process
                return redirect('currenttodos') # import redirect first
            except IntegrityError: # if user already exist
                return render(request, 'todo/signupuser.html', {'form':UserCreationForm(), 'error':'Username already exist!'})
        else:
            return render(request, 'todo/signupuser.html', {'form':UserCreationForm(), 'error':'Passwords didnt match!'})

def logoutuser(request):
    if request.method == 'POST':
        logout(request)
        return redirect('home')

def signinuser(request):
    if request.method == 'GET':
        # Sign In Form from Django
        return render(request, 'todo/signinuser.html', {'form':AuthenticationForm()})
    else:
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'todo/signinuser.html', {'form':AuthenticationForm(), 'error':'User not found!'})
        else:
            login(request, user) # login process
            return redirect('currenttodos') # import redirect first

def currenttodos(request):
    todos = Todo.objects.filter(user=request.user, dateCompleted__isnull=True) # get user to do data from Todo Models
    return render(request, 'todo/currenttodos.html', {'todos':todos})

def createtodos(request):
    if request.method == 'GET':
        return render(request, 'todo/createtodo.html', {'form':TodoForm()})
    else:
        try:
            form = TodoForm(request.POST)
            # commit=False is to not to save to database, remove it to save data to database
            newTodo = form.save(commit=False)
            newTodo.user = request.user # get the user
            newTodo.save() # then you can save it
            return redirect('currenttodos')
        except ValueError:
            return render(request, 'todo/createtodo.html', {'form':TodoForm(), 'error':'Bad data passed in! Try again Sir!'})