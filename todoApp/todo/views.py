from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm # Signup & Signin Form
from django.contrib.auth.models import User # to Make User
from django.db import IntegrityError # so the username is unique
from django.contrib.auth import login, logout, authenticate # for login & logout
from .forms import TodoForm # import forms.py
from .models import Todo # import Todo Model to get the data of Todo
from django.utils import timezone # for timeone heheh
from django.contrib.auth.decorators import login_required # only logged in user can access this view

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

@login_required
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

@login_required
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

@login_required
def currenttodos(request):
    todos = Todo.objects.filter(user=request.user, dateCompleted__isnull=True) # get user to do data from Todo Models
    return render(request, 'todo/currenttodos.html', {'todos':todos})

@login_required
def viewtodo(request, todo_pk):
    todo = get_object_or_404(Todo, pk=todo_pk, user=request.user) # got this from portofolio blog hehe
    if request.method == 'GET': # to view the detail
        form = TodoForm(instance=todo)
        return render(request, 'todo/viewtodo.html', {'todo':todo, 'form':form})
    else: # if any update
        try:
            form = TodoForm(request.POST, instance=todo)
            form.save()
            return redirect('currenttodos')
        except ValueError:
            return render(request, 'todo/viewtodo.html', {'todo':todo, 'form':form, 'error':'Bad data passed in! Try again Sir!'})

@login_required
def completetodo(request, todo_pk):
    todo = get_object_or_404(Todo, pk=todo_pk, user=request.user)
    if request.method == 'POST':
        todo.dateCompleted = timezone.now()
        todo.save()
        return redirect('currenttodos')

@login_required 
def deletetodo(request, todo_pk):
    todo = get_object_or_404(Todo, pk=todo_pk, user=request.user)
    if request.method == 'POST':
        todo.delete()
        return redirect('currenttodos')

@login_required
def completedtodos(request):
    todos = Todo.objects.filter(user=request.user, dateCompleted__isnull=False).order_by('dateCompleted')
    return render(request, 'todo/completetodos.html', {'todos':todos})