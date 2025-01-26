from django.contrib.auth.models import User
from django.urls import reverse
from django.test import TestCase
from .forms import CommentForm, TopicForm
from .models import Topic, Comment

# Create your tests here.

class TestTopicViews(TestCase):

    def setUp(self):
        self.user = User.objects.create_superuser(
            username="myUsername",
            password="myPassword",
            email="test@test.com"
        )
        self.client.login(username="myUsername", password="myPassword")
        self.topic = Topic.objects.create(
            title="Topic title",
            author=self.user,
            slug="topic-title",
            excerpt="Topic excerpt",
            content="Topic content",
            published=True
        )
        self.client.logout()  # Ensure the client is logged out for the next test

    def test_render_topic_detail_page_with_comment_form(self):
        self.client.login(username="myUsername", password="myPassword")
        response = self.client.get(reverse('topic_detail', args=['topic-title']))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Topic title", response.content)
        self.assertIn(b"Topic content", response.content)
        self.assertIsInstance(response.context['form'], CommentForm)

    def test_user_can_access_topic_page_from_home_page(self):
        self.client.login(username="myUsername", password="myPassword")
        response = self.client.get(reverse('landing_page'))
        self.assertEqual(response.status_code, 200)
        topic_url = reverse('topic_detail', args=['topic-title'])

        self.assertContains(response, f'href="{topic_url}"')

    def test_admin_can_post_content(self):
        self.client.login(username="myUsername", password="myPassword")
        response = self.client.post(reverse('create_topic'), {
            'title': 'New Topic',
            'slug': 'new-topic',
            'excerpt': 'New Topic Excerpt',
            'content': 'New Topic Content',
            'published': True,
            'author': self.user.id
        })
        self.assertEqual(response.status_code, 302)  # Redirect after successful post
        new_topic = Topic.objects.get(slug='new-topic')
        self.assertEqual(new_topic.title, 'New Topic')
        self.assertEqual(new_topic.content, 'New Topic Content')
        self.assertEqual(new_topic.author, self.user)

    def test_user_can_create_comment(self):
        self.client.login(username="myUsername", password="myPassword")
        response = self.client.post(reverse('create_comment', args=[self.topic.pk]), {
            'body': 'This is a test comment',
            'parent': ''
        })
        self.assertEqual(response.status_code, 302)  # Redirect after successful post
        new_comment = Comment.objects.get(body='This is a test comment')
        self.assertEqual(new_comment.body, 'This is a test comment')
        self.assertEqual(new_comment.author, self.user)
        self.assertEqual(new_comment.topic, self.topic)

    def test_user_can_edit_comment(self):
        self.client.login(username="myUsername", password="myPassword")
        comment = Comment.objects.create(
            body='Original comment',
            author=self.user,
            topic=self.topic
        )
        response = self.client.post(reverse('edit_comment', args=[comment.pk]), {
            'body': 'Edited comment'
        })
        self.assertEqual(response.status_code, 302)  # Redirect after successful post
        edited_comment = Comment.objects.get(pk=comment.pk)
        self.assertEqual(edited_comment.body, 'Edited comment')

    def test_user_can_delete_comment(self):
        self.client.login(username="myUsername", password="myPassword")
        comment = Comment.objects.create(
            body='Comment to be deleted',
            author=self.user,
            topic=self.topic
        )
        response = self.client.post(reverse('delete_comment', args=[comment.pk]))
        self.assertEqual(response.status_code, 302)  # Redirect after successful post
        with self.assertRaises(Comment.DoesNotExist):
            Comment.objects.get(pk=comment.pk)

    def test_user_can_like_and_unlike_topic(self):
        self.client.login(username="myUsername", password="myPassword")
        response = self.client.post(reverse('like_topic', args=[self.topic.pk]))
        self.assertEqual(response.status_code, 200)
        self.assertTrue(self.topic.likes.filter(pk=self.user.pk).exists())
        response = self.client.post(reverse('like_topic', args=[self.topic.pk]))
        self.assertEqual(response.status_code, 200)
        self.assertFalse(self.topic.likes.filter(pk=self.user.pk).exists())

    def test_redirect_to_login_if_not_logged_in(self):
        response = self.client.get(reverse('topic_detail', args=['topic-title']))
        self.assertRedirects(response, f"{reverse('login')}?next={reverse('topic_detail', args=['topic-title'])}")