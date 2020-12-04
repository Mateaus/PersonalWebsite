from django.db import models
from datetime import datetime
from django.utils.timezone import now

# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=64, null=False)
    description = models.TextField()
    data_added = models.DateTimeField(default=now, editable=False)
    last_modified_date = models.DateTimeField(auto_now=True)