from django.db import models


class Tag(models.Model):
    name = models.CharField(max_length=32)
    creation_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
