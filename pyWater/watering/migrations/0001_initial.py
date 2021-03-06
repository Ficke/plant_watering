# Generated by Django 3.2.9 on 2021-11-09 22:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Plant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('plant_name', models.CharField(max_length=200)),
                ('added_date', models.DateField(verbose_name='date added')),
                ('user', models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Plant', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Watering',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('water_date', models.DateField(verbose_name='date watered')),
                ('watered_plant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='plants', related_query_name='watering', to='watering.plant')),
            ],
            options={
                'ordering': ['water_date'],
            },
        ),
    ]
