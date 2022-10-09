from django.contrib.auth.models import User
from django.core.files.uploadedfile import SimpleUploadedFile
from django.forms import model_to_dict
from django.test import TestCase
from django.urls import reverse

from app_userauth.models import UserProfile


class ProfileEditTest(TestCase):

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
        cls.test_profile = UserProfile.objects.create(user=cls.test_user)
        cls.test_profile.save()

    def setUp(self):
        self.client.force_login(self.test_user)

    def tearDown(self):
        self.client.logout()

    def test_available_in_desired_path(self):
        url = '/profile/edit'
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_uses_correct_template(self):
        response = self.client.get(reverse('user_profile_edit'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'app_userauth/userprofile_edit.html')

    def test_login_required(self):
        response = self.client.get(reverse('user_profile_edit'))
        self.assertEqual(response.status_code, 200, 'Authenticated user cannot access the profile edit page')
        self.client.logout()
        response = self.client.get(reverse('user_profile_edit'), follow=True)
        self.assertEqual(response.status_code, 404, 'Unauthenticated user can access the profile edit page')

    def test_profile_edit(self):
        response = self.client.get(reverse('user_profile_edit'))
        self.assertEqual(response.status_code, 200)

        response = self.client.post(
            reverse('user_profile_edit'),
            self.TEST_PROFILE_CREDS
        )

        self.assertEqual(response.status_code, 200)
        if (response.context and
                response.context.get('profile')):
            form_errors = dict(response.context['profile'].errors)
            self.assertFalse(bool(form_errors),
                             f'Form error: {dict(form_errors)}' if form_errors else None)

        self.assertTrue(response.context['profile_is_saved'])

        # проверяем соответствие отправленных и сохранённых данных
        fields = ['first_name', 'last_name', 'about']
        new_profile_data = {
            k: v for k, v in self.TEST_PROFILE_CREDS.items() if k in fields
        }
        self.test_profile.refresh_from_db()
        self.assertEqual(
            model_to_dict(self.test_profile, fields=fields),
            new_profile_data,
        )
