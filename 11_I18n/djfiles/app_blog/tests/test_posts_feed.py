import datetime

from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse

from app_blog.models import BlogRecord


class PostsFeedTest(TestCase):

    NUMBER_OF_POSTS = 5

    @classmethod
    def setUpTestData(cls):
        # наполнение БД
        author = User.objects.create_user(
            username='TestUser',
            email='test@email.com',
            password='testpassword'
        )
        for item_index in range(cls.NUMBER_OF_POSTS):
            BlogRecord.objects.create(
                title=f'Post {item_index} title',
                body=f'Post {item_index} body',
                created=datetime.datetime.now(),
                author=author,
                cover=f'https://source.unsplash.com/random/700x400?sig={item_index}'
            )

    def test_posts_feed_exists_in_desired_location(self):
        url = '/'
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    #  Не знаю, есть смысл тестить передачу контекста и шаблона в ListView?
    #  Хотя, завтра вьюху могут и переписать...
    # TODO передачей контекста в шаблон занимается код фреймверка, а он уже имеет свои тесты, поэтому ответ - конечно же
    #  нет, тестируем только свой, привнесённый вами в проект, код
    def test_posts_number(self):
        response = self.client.get(reverse('records_list'))
        self.assertEqual(response.status_code, 200)
        self.assertTrue(len(response.context['object_list']) == self.NUMBER_OF_POSTS)

    def test_feed_uses_correct_template(self):
        response = self.client.get(reverse('records_list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'app_blog/blogrecord_list.html')

    def test_feed_uses_correct_context(self):
        response = self.client.get(reverse('records_list'))
        self.assertEqual(response.status_code, 200)
        self.assertIsNotNone(response.context.get('object_list'))
        posts = BlogRecord.objects.all()
        self.assertEqual(list(response.context['object_list'].values()), list(posts.values()))
