from django.contrib.auth.models import User
from django.core.files.uploadedfile import SimpleUploadedFile
from django.test import TestCase
from django.urls import reverse

from app_blog.models import BlogRecord


class AddBlogRecordTest(TestCase):

    TEST_COVER_GIF = (
        b'\x47\x49\x46\x38\x39\x61\x01\x00\x01\x00\x00\x00\x00\x21\xf9\x04'
        b'\x01\x0a\x00\x01\x00\x2c\x00\x00\x00\x00\x01\x00\x01\x00\x00\x02'
        b'\x02\x4c\x01\x00\x3b'
    )

    TEST_USER_CREDS = {
        'username': 'testuser',
        'password': 'testpassword'
    }
    RAW_POST = {
        'title': f'Post title',
        'body': f'Post body',
        'cover': SimpleUploadedFile(name='test_cover.jpg', content=TEST_COVER_GIF, content_type='image/gif')
    }

    @classmethod
    def setUpTestData(cls):
        cls.test_user = User.objects.create(username=cls.TEST_USER_CREDS['username'])
        cls.test_user.set_password(cls.TEST_USER_CREDS['password'])
        cls.test_user.save()
        # TODO для всего этого есть специальный метод - User.objects.create_user

    def setUp(self):
        self.client.force_login(self.test_user)  # TODO стоило придумать более сложный пароль и пользоваться login
                                                 #  вместо force_login

    def tearDown(self):
        self.client.logout()

    def test_available_in_desired_path(self):
        url = f'/record/add'
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_uses_correct_template(self):
        # TODO лишний тест, в этом представлении ведь не разные шаблоны в зависимости от каких-то условий
        response = self.client.get(reverse('add_record'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'app_blog/blogrecord_edit.html')

    def test_login_required(self):
        response = self.client.get(reverse('add_record'))
        self.assertEqual(response.status_code, 200, 'Authenticated user cannot access the post creation page')
        self.client.logout()
        response = self.client.get(reverse('add_record'), follow=True)
        self.assertEqual(response.status_code, 404, 'Unauthenticated user can access the post creation page')

    def test_post_add(self):
        response = self.client.get(reverse('add_record'))
        self.assertEqual(response.status_code, 200)

        # чистим таблицу постов
        BlogRecord.objects.all().delete()

        response = self.client.post(
            reverse('add_record'),
            self.RAW_POST
        )
        # если вместо редиректа вернулась форма, то значит в ней есть ошибки:
        form_errors = {}
        if (response.context and
                response.context.get('form') and
                response.context['form'].errors):
            form_errors = dict(response.context['form'].errors)
        self.assertEqual(response.status_code, 302,
                         f'Form error: {dict(form_errors)}' if form_errors else None)
        self.assertEqual(len(BlogRecord.objects.all()), 1, 'Post is not added to the database or added many times')
        #  Стоит полностью проверять артефакты, создаваемые в процессе работы метода
        #  (в данном случае все поля BlogRecord) или достаточно проверять их количество
        #  (мол, мы тут тестируем вьюху, в БД что-то упало - значит вьюха отработала)?
        #  С одной стороны: вьюха отработала - все молодцы.
        #  С другой - если во вьюхе или форме происходила (или будет происходить) промежуточная обработка данных,
        #  то такой тест не покажет их некорректную обработку
        # TODO Если какой-то сложной логики при создании записи из переданных представлению данных формы нет, то
        #  проверяем только результат добавления записи - запись создалась или нет. И наоборот - если исходные данные
        #  преобразуются "дополнительной" логикой, то конечно это тоже стоит проверить отдельно.
