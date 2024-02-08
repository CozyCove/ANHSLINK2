# Generated by Django 5.0.1 on 2024-02-07 08:59

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_alter_resources_file'),
    ]

    operations = [
        migrations.AddField(
            model_name='resources',
            name='uuid',
            field=models.UUIDField(default=uuid.uuid4, editable=False, unique=True),
        ),
    ]
