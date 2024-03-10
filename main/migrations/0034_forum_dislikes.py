# Generated by Django 5.0.1 on 2024-03-10 13:09

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0033_remove_comment_likes_forum_likes_delete_like'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='forum',
            name='dislikes',
            field=models.ManyToManyField(related_name='disliked_comments', to=settings.AUTH_USER_MODEL),
        ),
    ]
