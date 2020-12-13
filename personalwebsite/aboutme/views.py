from django.shortcuts import render
from .models import Introduction, IntroductionContent, Section, SectionContent

# Create your views here.
def about_me(request):
    introduction = Introduction.objects.all().first()
    sections = Section.objects.all().order_by('pk')

    context = {
        "introduction": introduction,
        "sections": sections,
    }

    return render(request, 'aboutme/about_me_page_view.html', context=context)