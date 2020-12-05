from django.shortcuts import render
from .models import Project

# Create your views here.
def projects(request):
    all_projects = Project.objects.all()
    context = {
        'all_projects': all_projects
    }
    return render(request, 'projects.html', context)
