from django.contrib.auth.models import User
from django.core.files.uploadedfile import SimpleUploadedFile
from django.test import TestCase
from django.urls import reverse

from app_userauth.models import UserProfile


class PostsFeedTest(TestCase):
    TEST_AVATAR_GIF = (
        b'\x47\x49\x46\x38\x39\x61\x01\x00\x01\x00\x00\x00\x00\x21\xf9\x04'
        b'\x01\x0a\x00\x01\x00\x2c\x00\x00\x00\x00\x01\x00\x01\x00\x00\x02'
        b'\x02\x4c\x01\x00\x3b'
    )

    TEST_USER_CREDS = {
        'username': 'testuser',
        'password': 'testpassword'
    }

    TEST_PROFILE_CREDS = {
        'first_name': 'TestUserFirstName',
        'last_name': 'TestUserLastName',
        'about': 'TestUserAbout',
        'avatar': SimpleUploadedFile(name='test_avatar.gif', content=TEST_AVATAR_GIF, content_type='image/gif')
    }

    @classmethod
    def setUpTestData(cls):
        cls.test_user = User.objects.create(username=cls.TEST_USER_CREDS['username'])
        cls.test_user.set_password(cls.TEST_USER_CREDS['password'])
        cls.test_user.save()
        cls.test_profile = UserProfile.objects.create(user=cls.test_user, **cls.TEST_PROFILE_CREDS)
        cls.test_profile.save()

    def test_exists_in_desired_location(self):
        url = f'/profile/{self.test_user.id}'
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_uses_correct_template(self):
        response = self.client.get(reverse('user_profile_detail', kwargs={'pk': self.test_user.id}))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'app_userauth/userprofile_detail.html')

    def test_uses_correct_context(self):
        response = self.client.get(reverse('user_profile_detail', kwargs={'pk': self.test_user.id}))
        self.assertEqual(response.status_code, 200)
        self.assertIsNotNone(response.context.get('object'))
        self.assertEqual(response.context['object'], self.test_profile)
