# Generated by Django 5.0.1 on 2024-02-18 13:30

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0014_alter_forum_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='forum',
            name='slug',
            field=models.SlugField(default=uuid.uuid1),
        ),
    ]
