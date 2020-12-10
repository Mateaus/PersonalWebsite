# Generated by Django 3.1.3 on 2020-12-10 06:49

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=64)),
                ('description', models.TextField()),
                ('cover_image', models.ImageField(blank=True, upload_to='project/cover_images/')),
                ('data_added', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('last_modified_date', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
