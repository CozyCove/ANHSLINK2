# Generated by Django 5.0.1 on 2024-02-06 02:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_alter_resources_file'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resources',
            name='file',
            field=models.FileField(upload_to='media/'),
        ),
    ]
