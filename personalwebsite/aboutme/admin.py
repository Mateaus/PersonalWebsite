from django.contrib import admin
from .models import Introduction, IntroductionContent, Section, SectionContent


class IntroductionContentInline(admin.TabularInline):
    model = IntroductionContent


@admin.register(Introduction)
class IntroductionAdmin(admin.ModelAdmin):
    list_display = ['title', 'profile_image']
    inlines = [
        IntroductionContentInline
    ]

    def has_add_permission(self, request):
        """ 
        Allows the admin to only add a single entry for Introduction.
        """
        return Introduction.objects.all().count() == 0


class SectionContentInline(admin.TabularInline):
    model = SectionContent


@admin.register(Section)
class SectionAdmin(admin.ModelAdmin):
    list_display = ['title']
    ordering = ['pk']
    inlines = [
        SectionContentInline
    ]
