# Generated by Django 5.0.1 on 2024-02-08 00:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_resources_uuid'),
    ]

    operations = [
        migrations.AddField(
            model_name='resources',
            name='name',
            field=models.CharField(default='Default Name', max_length=100),
        ),
    ]
