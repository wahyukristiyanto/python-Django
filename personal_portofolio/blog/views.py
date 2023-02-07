from django.shortcuts import render, get_object_or_404
from .models import Project

# Create your views here.
def all_blogs(request):
    # projects = Project.objects.all()

    # [:number] is view limiter
    projects = Project.objects.order_by('-date')[:3]
    
    return render(request, 'blog/all_blogs.html', {'projects':projects})

def details(request, blog_id):
    blog = get_object_or_404(Project, pk=blog_id)
    return render(request, 'blog/details.html', {'blog':blog})