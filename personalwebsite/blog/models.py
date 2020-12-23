from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from tinymce.models import HTMLField


class Tag(models.Model):
    name = models.CharField(max_length=56)

    def __str__(self):
        return self.name


class PostOverview(models.Model):
    title = models.CharField(max_length=256)
    overview = models.TextField()
    tags = models.ManyToManyField(Tag)
    estimated_time = models.IntegerField()
    creation_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)


class PostDetail(models.Model):
    post_overview = models.OneToOneField(
        PostOverview, on_delete=models.CASCADE)
    content = HTMLField()
    previous_post = models.ForeignKey('self', related_name='previous', on_delete=models.SET_NULL, blank=True, null=True)
    next_post = models.ForeignKey('self', related_name='next', on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return self.post_overview.title
