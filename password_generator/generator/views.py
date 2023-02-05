from django.shortcuts import render
from django.http import HttpResponse
import random

# Create your views here.

def beranda(request):
    return render(request, 'generator/beranda.html')

def password(request):

    characters = list('abcdefghijklmnopqrstuvwxyz')

    if request.GET.get('uppercase'):
        characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))

    if request.GET.get('numbers'):
        characters.extend(list('0123456789'))

    if request.GET.get('special'):
        characters.extend(list('~!@#$%^&*()_+-=<>?:'))

    length = int(request.GET.get('length','12'))
    
    thePassword = ''

    for x in range(length):
        thePassword += random.choice(characters)

    return render(request, 'generator/password.html', {'password':thePassword})

def tentang(request):
    return render(request, 'generator/tentang.html', {'text':'Tentang'})