from django.contrib import admin
# Register your models here.
from .models import Introduction, Section, SectionContent

admin.site.register(Section)
admin.site.register(SectionContent)

@admin.register(Introduction)
class IntroductionModelAdmin(admin.ModelAdmin):

    def has_add_permission(self, request):
        """ 
        Allows the admin to only add a single entry for Introduction.
        """
        return Introduction.objects.all().count() == 0
