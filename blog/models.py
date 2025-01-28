from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
from cloudinary.models import CloudinaryField

# Create your models here.


class Topic(models.Model):
    CATEGORY_OPTION = [
        ('nuclear_facilities', 'Nuclear Facilities'),
        ('nuclear_fuel_waste', 'Nuclear Fuel & Waste'),
        ('nuclear_defence', 'Nuclear Defence'),
        ('nuclear_power_space', 'Nuclear Power in Space'),
        ('fact_or_fiction', 'Fact or Fiction'),
        ('educational_resources', 'Educational Resources'),
    ]

    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=300, unique=True, blank=True)
    content = models.TextField()
    excerpt = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    published = models.BooleanField(default=False)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    likes = models.ManyToManyField(
        User, related_name='liked_topics', blank=True
    )
    image = CloudinaryField(
        'image', blank=True, null=True, default='placeholder.png'
    )
    alt_description = models.CharField(
        max_length=255, blank=True, null=True
    )
    category = models.CharField(
        max_length=200, choices=CATEGORY_OPTION, default='nuclear_facilities'
    )

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title


class Comment(models.Model):
    topic = models.ForeignKey(
        Topic, on_delete=models.CASCADE, related_name='comments'
    )
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    parent = models.ForeignKey(
        'self', null=True, blank=True, on_delete=models.CASCADE,
        related_name='replies'
    )

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return f'Comment by {self.author.username} on {self.topic.title}'
