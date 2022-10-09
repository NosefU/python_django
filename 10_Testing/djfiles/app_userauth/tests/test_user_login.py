from django.contrib.auth.models import User
from django.contrib.sessions.models import Session
from django.test import TestCase
from django.urls import reverse


class LoginTest(TestCase):

    TEST_USER_CREDS = {
        'username': 'testuser',
        'password': 'testpassword'
    }

    @classmethod
    def setUpTestData(cls):
        cls.test_user = User.objects.create(username=cls.TEST_USER_CREDS['username'])
        cls.test_user.set_password(cls.TEST_USER_CREDS['password'])
        cls.test_user.save()

    def test_available_in_desired_path(self):
        url = '/login'
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_uses_correct_template(self):
        response = self.client.get(reverse('login'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed('app_userauth/login.html')

    def test_login(self):
        sessions_before_login = len(Session.objects.all())

        response = self.client.get(reverse('login'))
        self.assertEqual(response.status_code, 200)

        response = self.client.post(
            reverse('login'),
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

        sessions_after_login = len(Session.objects.all())
        self.assertGreaterEqual(sessions_after_login - sessions_before_login, 1, 'User not logged in')
