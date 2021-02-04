from django.contrib import admin
from django.core.exceptions import ValidationError
from django import forms
from .models import Project, Image, ImageAlbum
from django.utils.safestring import mark_safe
from django.utils.html import format_html
from django.db.models import Q


class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = "__all__"

    def clean(self):
        cleaned_data = self.cleaned_data
        tags = cleaned_data['tags']
        if len(tags) > 8:
            raise ValidationError("You can't assign more than 8 tags to a project.")
        return cleaned_data


class ImageForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ['name', 'image', 'default', 'album']

    def clean(self):
        cleaned_data = self.cleaned_data
        default = cleaned_data['default']
        try:
            image_album = ImageAlbum.objects.get(pk=cleaned_data['album'].pk)
        except AttributeError:
            return cleaned_data

        # does this album already have a default image set?
        if image_album and default:
            for image in image_album.images.all():
                if image.default:
                    raise ValidationError("This image album already has a default set.")
        
        return cleaned_data



@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    form = ProjectForm
    filter_horizontal = ('tags',)


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    form = ImageForm


class ImageAlbumForm(forms.ModelForm):
    class Meta:
        model = ImageAlbum
        fields = ['name']


@admin.register(ImageAlbum)
class ImageAlbumAdmin(admin.ModelAdmin):
    form = ImageAlbumForm
    list_display = ('name', 'date_created', 'default')
    readonly_fields = ('images',)

    def images(self, album):
        if len(album.images.all()) != 0:
            album_images = []
            for obj in album.images.all():
                album_images.append('<img src="{}" style="width: 150px; height:100px; margin-right: 10px" />'.format(obj.image.url))
            album_images = "".join(album_images)
            return format_html(album_images)
        return None

    def default(self, album):
        album_cover_img = album.images.filter(default=True).first()
        if (album_cover_img):
            return format_html('<img src="{}" style="width: 150px; height:100px;" />'.format(album_cover_img.image.url))
        return
