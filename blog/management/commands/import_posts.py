from django.core.management.base import BaseCommand
from blog.models import Topic
import json
from django.contrib.auth.models import User
from django.utils.text import slugify

class Command(BaseCommand):
    help = 'Import blog posts from JSON file'

    def handle(self, *args, **options):
        with open('blog/fixtures/nuclear_facilities_posts.json', 'r') as file:
            posts = json.load(file)

        default_user = User.objects.get(username='')  # Change this to an existing user

        for post in posts:
            slug = slugify(post['title'])
            # Ensure the slug is unique
            unique_slug = slug
            counter = 1
            while Topic.objects.filter(slug=unique_slug).exists():
                unique_slug = f"{slug}-{counter}"
                counter += 1

            Topic.objects.create(
                title=post['title'],
                content=post['content'],
                author=default_user,
                created_at=post['created_at'],
                image=post['image'],
                alt_description=post['alt_description'],
                slug=unique_slug
            )

        self.stdout.write(self.style.SUCCESS('Successfully imported blog posts'))
