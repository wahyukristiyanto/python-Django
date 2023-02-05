from django.shortcuts import render
from .models import Project

# Create your views here.
def all_blogs(request):
    projects = Project.objects.all()
    return render(request, 'blog/all_blogs.html', {'projects':projects})