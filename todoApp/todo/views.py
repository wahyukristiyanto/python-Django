from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def signupuser(request):
    # Sign Up Form from Django
    return render(request, 'todo/signupuser.html', {'form':UserCreationForm()})