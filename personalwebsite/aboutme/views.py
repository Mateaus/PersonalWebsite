from django.shortcuts import render
from .models import Introduction, IntroductionContent, Section, SectionContent

# Create your views here.
def about_me(request):
    introduction = Introduction.objects.all().first()
    introduction_contents = IntroductionContent.objects.all()
    sections = Section.objects.all()
    section_contents = SectionContent.objects.all()

    context = {
        "introduction": introduction,
        "introduction_contents": introduction_contents,
        "sections": sections,
        "contents": section_contents
    }

    return render(request, 'aboutme/about_me_page_view.html', context=context)