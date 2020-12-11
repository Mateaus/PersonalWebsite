from django.contrib import admin
from .models import Introduction, IntroductionContent, Section, SectionContent

admin.site.register(Section)
admin.site.register(SectionContent)
admin.site.register(IntroductionContent)

@admin.register(Introduction)
class IntroductionModelAdmin(admin.ModelAdmin):

    def has_add_permission(self, request):
        """ 
        Allows the admin to only add a single entry for Introduction.
        """
        return Introduction.objects.all().count() == 0
