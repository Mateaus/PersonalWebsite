from django.contrib import admin
from django.core.exceptions import ValidationError
from django import forms
from .models import Project, Image, ImageAlbum
from django.utils.safestring import mark_safe
from django.utils.html import format_html


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


class ImageForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ['name', 'image', 'default', 'album']


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    form = ProjectForm
    filter_horizontal = ('tags',)


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    form = ImageForm


@admin.register(ImageAlbum)
class ImageAlbumAdmin(admin.ModelAdmin):
    list_display = ('name', 'date_created', 'default')
    readonly_fields = ('images',)    

    def default(self, album):
        return format_html('<img src="{}" style="width: 150px; height:100px;" />'.format(album.images.filter(default=True).first().image.url))

    def images(self, album):
        album_images = []
        for obj in album.images.all():
            album_images.append('<img src="{}" style="width: 150px; height:100px; margin-right: 10px" />'.format(obj.image.url))
        album_images = "".join(album_images)
        return format_html(album_images)

