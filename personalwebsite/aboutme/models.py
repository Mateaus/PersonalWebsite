from django.db import models

# Create your models here.
class Section(models.Model):
    title = models.CharField(max_length=64)

    def __str__(self):
        return self.title

class SectionContent(models.Model):
    section = models.ForeignKey(Section, on_delete=models.CASCADE)
    title = models.CharField(max_length=64)
    content = models.CharField(max_length=256)

    def __str__(self):
        return self.title + " - " + self.content