# Generated by Django 3.1.3 on 2021-01-23 23:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0004_auto_20210123_2339'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='width',
            field=models.FloatField(default=100),
        ),
    ]