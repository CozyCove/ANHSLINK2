# Generated by Django 5.0.1 on 2024-02-20 06:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0024_dislike_like'),
    ]

    operations = [
        migrations.AlterField(
            model_name='forum',
            name='description',
            field=models.CharField(default='', max_length=240),
        ),
    ]
