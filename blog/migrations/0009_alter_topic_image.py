# Generated by Django 5.1.4 on 2025-01-17 17:34

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_topic_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='topic',
            name='image',
            field=cloudinary.models.CloudinaryField(blank=True, default='placeholder.png', max_length=255, null=True, verbose_name='image'),
        ),
    ]
