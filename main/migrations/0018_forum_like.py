# Generated by Django 5.0.1 on 2024-02-18 14:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0017_remove_forum_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='forum',
            name='like',
            field=models.IntegerField(default=316),
        ),
    ]