# Generated by Django 3.2.9 on 2021-11-08 20:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('watering', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='watering',
            options={'ordering': ['water_date']},
        ),
    ]