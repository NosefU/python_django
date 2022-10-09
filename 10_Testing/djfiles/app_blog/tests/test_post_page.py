import datetime

from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse

from app_blog.models import BlogRecord


class PostsFeedTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # наполнение БД
        author = User.objects.create_user(
            username='TestUser',
            email='test@email.com',
            password='testpassword'
        )

        cls.TEST_POST = BlogRecord.objects.create(
            title=f'Post title',
            body=f'Post body',
            created=datetime.datetime.now(),
            author=author,
            cover=f'https://source.unsplash.com/random/700x400?sig=1'
        )

    def test_posts_page_exists_in_desired_location(self):
        url = f'/record/{self.TEST_POST.id}'
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_post_uses_correct_template(self):
        response = self.client.get(reverse('record_page', kwargs={'pk': self.TEST_POST.id}))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'app_blog/blogrecord_detail.html')

    def test_post_page_uses_correct_context(self):
        response = self.client.get(reverse('record_page', kwargs={'pk': self.TEST_POST.id}))
        self.assertEqual(response.status_code, 200)
        self.assertIsNotNone(response.context.get('object'))
        self.assertEqual(response.context['object'], self.TEST_POST)
