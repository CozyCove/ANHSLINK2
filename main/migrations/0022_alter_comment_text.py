# Generated by Django 5.0.1 on 2024-02-19 02:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0021_remove_forum_comments_comment_author_comment_forum_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='text',
            field=models.CharField(max_length=200),
        ),
    ]