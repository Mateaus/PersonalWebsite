from django.db import models
from tag.models import Tag


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
    tags = models.ManyToManyField(Tag, blank=True)
    data_added = models.DateTimeField(auto_now_add=True)
    last_modified_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
