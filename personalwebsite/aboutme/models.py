from django.db import models

# Create your models here.
class Introduction(models.Model):
    profile_image = models.ImageField(upload_to='introduction', null=True, blank=True)
    title = models.CharField(max_length=256)

    def __str__(self):
        return "Introduction"

class IntroductionContent(models.Model):
    introduction = models.ForeignKey(Introduction, on_delete=models.CASCADE)
    paragraph = models.CharField(max_length=512)

    def __str__(self):
        return self.paragraph

class Section(models.Model):
    title = models.CharField(max_length=64)

    def __str__(self):
        return self.title

class SectionContent(models.Model):
    section = models.ForeignKey(Section, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='aboutme', null=True, blank=True)
    title = models.CharField(max_length=64)
    description = models.CharField(max_length=256)

    def __str__(self):
        return self.title + " - " + self.description