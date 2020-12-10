from django.db import models
from datetime import datetime
from django.utils.timezone import now


class Tag(models.Model):
    name = models.CharField(max_length=32)
    icon = models.ImageField(
        upload_to="project/tag/icons/",
        height_field=None,
        width_field=None,
        blank=True,
        null=True
    )


# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=64, null=False)
    description = models.TextField()
    cover_image = models.ImageField(
        upload_to="project/cover_images/", 
        height_field=None, 
        width_field=None, 
        blank=True,
        null=True
    )
    tags = models.ManyToManyField(Tag)
    data_added = models.DateTimeField(default=now, editable=False)
    last_modified_date = models.DateTimeField(auto_now=True)