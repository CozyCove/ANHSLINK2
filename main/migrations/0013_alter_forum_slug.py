# Generated by Django 5.0.1 on 2024-02-18 13:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0012_forum_slug_alter_forum_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='forum',
            name='slug',
            field=models.SlugField(blank=True, unique=True),
        ),
    ]
