from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm # Signup Form
from django.contrib.auth.models import User # to Make User
from django.db import IntegrityError # so the username is unique
from django.contrib.auth import login, logout # for login & logout

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

def currenttodos(request):
    return render(request, 'todo/currenttodos.html')

def logoutuser(request):
    if request.method == 'POST':
        logout(request)
        return redirect('home')