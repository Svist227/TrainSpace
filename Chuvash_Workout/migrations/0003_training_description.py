# Generated by Django 5.0.7 on 2024-08-15 08:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Chuvash_Workout', '0002_rename_programs_training'),
    ]

    operations = [
        migrations.AddField(
            model_name='training',
            name='description',
            field=models.SlugField(blank=True, default='1'),
        ),
    ]
