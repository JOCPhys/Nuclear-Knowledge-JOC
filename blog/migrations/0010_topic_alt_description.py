# Generated by Django 5.1.4 on 2025-01-19 18:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_alter_topic_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='topic',
            name='alt_description',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
