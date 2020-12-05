from django.shortcuts import render
from .models import Introduction, Section, SectionContent

# Create your views here.
def about_me(request):
    introduction = Introduction.objects.all().first()
    sections = Section.objects.all()
    section_contents = SectionContent.objects.all()

    context = {
        "introduction": introduction,
        "sections": sections,
        "contents": section_contents
    }

    return render(request, 'aboutme/about_me_page_view.html', context=context)