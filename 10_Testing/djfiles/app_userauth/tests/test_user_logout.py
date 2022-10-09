from django.contrib.auth.models import User
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

    def setUp(self):
        self.client.force_login(self.test_user)

    def tearDown(self):
        self.client.logout()

    def test_available_in_desired_path(self):
        url = '/logout'
        response = self.client.get(url)
        self.assertEqual(response.status_code, 302)

    def test_logout(self):
        from django.contrib.sessions.models import Session
        sessions_before_logout = len(Session.objects.all())

        response = self.client.get(reverse('logout'))
        self.assertEqual(response.status_code, 302)

        sessions_after_logout = len(Session.objects.all())
        self.assertLessEqual(sessions_before_logout - sessions_after_logout, 1, 'User not logged out')
