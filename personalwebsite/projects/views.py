from django.shortcuts import render

# Create your views here.
def projects(request):
    project_list = ['Project 1', 'Project 2', 'Project 3']
    context = {
        'project_list': project_list,
    }
    return render(request, 'project/projects.html', context)
