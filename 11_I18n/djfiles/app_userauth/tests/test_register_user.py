from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse

from app_userauth.models import UserProfile


class RegisterUserTest(TestCase):

    TEST_USER_CREDS = {
        'username': 'testuser',
        'password1': 'Test2020!Pass',
        'password2': 'Test2020!Pass'
    }

    def test_available_in_desired_path(self):
        url = '/register'
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_uses_correct_template(self):
        response = self.client.get(reverse('register'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'app_userauth/register.html')

    def test_register(self):
        response = self.client.get(reverse('register'))
        self.assertEqual(response.status_code, 200)

        # чистим таблицу пользователей
        User.objects.all().delete()

        response = self.client.post(
            reverse('register'),
            self.TEST_USER_CREDS
        )
        # если вместо редиректа вернулась форма, то значит в ней есть ошибки:
        form_errors = {}
        if (response.context and
                response.context.get('form') and
                response.context['form'].errors):
            form_errors = dict(response.context['form'].errors)
        self.assertEqual(response.status_code, 302,
                         f'Form error: {dict(form_errors)}' if form_errors else None)
        self.assertEqual(len(User.objects.all()), 1, 'User is not added to the database or added many times')
        self.assertEqual(
            len(UserProfile.objects.all()), 1,
            'UserProfile is not added to the database or added many times')
