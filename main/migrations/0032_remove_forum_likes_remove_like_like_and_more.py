# Generated by Django 5.0.1 on 2024-03-02 17:33

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0005_alter_profile_section'),
        ('main', '0031_alter_forum_description'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='forum',
            name='likes',
        ),
        migrations.RemoveField(
            model_name='like',
            name='like',
        ),
        migrations.AlterField(
            model_name='forum',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='author', to='authentication.profile'),
        ),
        migrations.DeleteModel(
            name='Dislike',
        ),
    ]
