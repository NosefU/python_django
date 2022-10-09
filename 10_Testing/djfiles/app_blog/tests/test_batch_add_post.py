from django.contrib.auth.models import User
from django.core.files.uploadedfile import SimpleUploadedFile
from django.test import TestCase
from django.urls import reverse

from app_blog.models import BlogRecord


class BatchAddBlogRecordTest(TestCase):

    TEST_USER_CREDS = {
        'username': 'testuser',
        'password': 'testpassword'
    }
    TEST_CSV = 'date;title;cover;body\n' \
               '2022-03-26 23:10:18;"Post 1 title";https://cs12.pikabu.ru/post_img/2022/03/19/9/1647699259268381776.webp;"Post 1 body"\n' \
               ';;;"Post 2 body"'

    RAW_POST_DATA = {
        'posts_file': SimpleUploadedFile(
            name='posts.csv',
            content=TEST_CSV.encode('UTF-8'),
            content_type='text/csv'
        )
    }


    @classmethod
    def setUpTestData(cls):
        cls.test_user = User.objects.create(username=cls.TEST_USER_CREDS['username'])
        cls.test_user.set_password(cls.TEST_USER_CREDS['password'])
        cls.test_user.save()

    def setUp(self):
        self.client.force_login(self.test_user)

    def tearDown(self):
        self.client.logout()

    def test_available_in_desired_path(self):
        url = f'/record/batch_add'
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_uses_correct_template(self):
        response = self.client.get(reverse('batch_add_record'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'app_blog/blogrecord_batch_add.html')

    def test_login_required(self):
        response = self.client.get(reverse('batch_add_record'))
        self.assertEqual(response.status_code, 200, 'Authenticated user cannot access the post creation page')
        self.client.logout()
        response = self.client.get(reverse('batch_add_record'), follow=True)
        self.assertEqual(response.status_code, 404, 'Unauthenticated user can access the post creation page')

    def test_post_batch_add(self):
        response = self.client.get(reverse('batch_add_record'))
        self.assertEqual(response.status_code, 200)

        # чистим таблицу постов
        BlogRecord.objects.all().delete()

        response = self.client.post(
            reverse('batch_add_record'),
            self.RAW_POST_DATA
        )
        # если вместо редиректа вернулась форма, то значит в ней есть ошибки:
        form_errors = {}
        if (response.context and
                response.context.get('form') and
                response.context['form'].errors):
            form_errors = dict(response.context['form'].errors)
        self.assertEqual(response.status_code, 302,
                         f'Form error: {dict(form_errors)}' if form_errors else None)
        self.assertEqual(len(BlogRecord.objects.all()), 2, 'Posts is not added to the database or added many times')
