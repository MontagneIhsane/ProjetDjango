# Generated by Django 5.1.4 on 2025-01-09 09:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carte', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='carte',
            name='titre',
            field=models.CharField(default='Untitled', max_length=255),
        ),
    ]