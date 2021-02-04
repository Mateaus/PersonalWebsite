from django.db import models
from tag.models import Tag


def get_upload_path(instance, filename):
    model = instance.album.model.__class__._meta
    name = model.verbose_name_plural.replace(' ', '_')
    return f'{name}/project/images/{filename}'


class ImageAlbum(models.Model):
    name = models.CharField(max_length=64)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    

class Image(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to="project/cover_images/")
    default = models.BooleanField(default=False)
    width = models.FloatField(default=100)
    length = models.FloatField(default=100)
    album = models.ForeignKey(ImageAlbum, related_name='images', on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.name
    

class Project(models.Model):
    title = models.CharField(max_length=64, null=False)
    description = models.TextField(max_length=389)
    tags = models.ManyToManyField(Tag, blank=True)
    data_added = models.DateTimeField(auto_now_add=True)
    last_modified_date = models.DateTimeField(auto_now=True)
    album = models.OneToOneField(ImageAlbum, related_name="model", on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.title