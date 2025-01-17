# Generated by Django 5.1.4 on 2025-01-17 11:47

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_alter_comment_options_topic_likes'),
    ]

    operations = [
        migrations.AddField(
            model_name='topic',
            name='image',
            field=cloudinary.models.CloudinaryField(blank=True, max_length=255, null=True, verbose_name='image'),
        ),
    ]