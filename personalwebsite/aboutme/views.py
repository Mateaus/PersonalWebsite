from django.views.generic.base import TemplateView

from .models import Introduction, Section


class AboutMeView(TemplateView):
    template_name = "aboutme/about_me_page_view.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['introduction'] = Introduction.objects.all().first()
        context['sections'] = Section.objects.all().order_by('pk')
        return context
