from django.db import models
from django.contrib.auth.models import User
from tinymce.models import HTMLField

class Tag(models.Model):
    name = models.CharField(max_length=56)

    def __str__(self):
        return self.name

class Post(models.Model):
    title = models.CharField(max_length=256)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    overview = models.TextField()
    estimated_time = models.IntegerField()
    creation_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)
    content = HTMLField()
    tags = models.ManyToManyField(Tag)


class Potato(models.Model):
    title = models.CharField(max_length=256)

class Root(models.Model):
    potato = models.OneToOneField(Potato, on_delete=models.CASCADE)
    content = HTMLField()