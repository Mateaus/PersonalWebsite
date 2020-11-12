from django.shortcuts import render

# Create your views here.
def about_me(request):
    return render(request, 'aboutme/about_me_page_view.html')