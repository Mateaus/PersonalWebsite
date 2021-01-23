# Generated by Django 3.1.3 on 2021-01-06 04:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('tag', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=64)),
                ('description', models.TextField()),
                ('cover_image', models.ImageField(blank=True, null=True, upload_to='project/cover_images/')),
                ('data_added', models.DateTimeField(auto_now_add=True)),
                ('last_modified_date', models.DateTimeField(auto_now=True)),
                ('tags', models.ManyToManyField(blank=True, to='tag.Tag')),
            ],
        ),
    ]
