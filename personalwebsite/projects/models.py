from django.db import models
from datetime import datetime
from django.utils.timezone import now

# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=64, null=False)
    description = models.TextField()
    cover_image = models.ImageField(
        upload_to="project/cover_images/", 
        height_field=None, 
        width_field=None, 
        null=True
    )
    data_added = models.DateTimeField(default=now, editable=False)
    last_modified_date = models.DateTimeField(auto_now=True)