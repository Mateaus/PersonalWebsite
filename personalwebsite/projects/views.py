from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Project

# Create your views here.
def projects(request):
    all_projects = Project.objects.all()
    paginator = Paginator(all_projects, 3)
    page = request.GET.get('page')

    try:
        project_list = paginator.page(page)
    except PageNotAnInteger:
        project_list = paginator.page(1)
    except EmptyPage:
        project_list = paginator.page(paginator.num_pages)

    context = {
        'all_projects': all_projects,
        'project_list': project_list
    }
    return render(request, 'projects.html', context)


def project_detail(request, pk):
    project = Project.objects.get(pk=pk)
    context = {
        'project': project
    }
    return render(request, "project_detail.html", context)
