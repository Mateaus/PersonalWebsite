# Generated by Django 3.1.3 on 2020-12-11 02:36

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0008_auto_20201210_0757'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tag',
            name='icon',
        ),
        migrations.AddField(
            model_name='tag',
            name='data_added',
            field=models.DateTimeField(default=django.utils.timezone.now, editable=False),
        ),
        migrations.AddField(
            model_name='tag',
            name='last_modified_date',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
