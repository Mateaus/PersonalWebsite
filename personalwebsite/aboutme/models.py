from django.db import models

# Create your models here.
class Introduction(models.Model):
    profile_image = models.ImageField(upload_to='introduction', null=True, blank=True)
    title = models.CharField(max_length=256)

    class Meta:
        verbose_name = 'Introduction'
        verbose_name_plural = verbose_name

class IntroductionContent(models.Model):
    introduction = models.ForeignKey(Introduction, on_delete=models.CASCADE)
    paragraph = models.CharField(max_length=512)

class Section(models.Model):
    title = models.CharField(max_length=64)

class SectionContent(models.Model):
    section = models.ForeignKey(Section, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='aboutme', null=True, blank=True)
    title = models.CharField(max_length=64)
    description = models.CharField(max_length=256)