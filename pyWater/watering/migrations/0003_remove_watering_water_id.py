# Generated by Django 3.2.9 on 2021-11-02 17:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('watering', '0002_rename_plants_plant'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='watering',
            name='water_id',
        ),
    ]