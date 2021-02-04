# Generated by Django 3.1.3 on 2021-01-24 00:07

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0006_auto_20210123_2348'),
    ]

    operations = [
        migrations.AddField(
            model_name='imagealbum',
            name='date_created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='imagealbum',
            name='name',
            field=models.CharField(default='name', max_length=64),
            preserve_default=False,
        ),
    ]