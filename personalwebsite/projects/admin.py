from django.contrib import admin
from django.core.exceptions import ValidationError
from django import forms
from .models import Project


class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = "__all__"

    def clean(self):
        cleaned_data = self.cleaned_data
        tags = cleaned_data['tags']
        if len(tags) > 8:
            raise ValidationError(
                "You can't assign more than 8 tags to a project.")
        return cleaned_data


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    form = ProjectForm
    filter_horizontal = ('tags',)
