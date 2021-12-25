from django.contrib.auth import get_user_model
from django.test import TestCase
from rest_framework import status
User = get_user_model()
class UsersManagersTests(TestCase):

    def test_create_user(self):
        user= User.objects.create_user(email='normal@user.com', name='normal', password='foo')
        self.assertEqual(user.email, 'normal@user.com')
        self.assertEqual(user.name, 'normal')
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)
        try:
            # username is None for the AbstractUser option
            # username does not exist for the AbstractBaseUser option
            self.assertIsNone(user.username)
        except AttributeError:
            pass
        with self.assertRaises(TypeError):
            User.objects.create_user()
        with self.assertRaises(TypeError):
            User.objects.create_user(email='')
        with self.assertRaises(ValueError):
            User.objects.create_user(email='', name='', password="foo")

    def test_create_superuser(self):
        User = get_user_model()
        admin_user = User.objects.create_superuser(email='super@user.com', name='super', password='foo')
        self.assertEqual(admin_user.email, 'super@user.com')
        self.assertEqual(admin_user.name, 'super')
        self.assertTrue(admin_user.is_active)
        self.assertTrue(admin_user.is_staff)
        self.assertTrue(admin_user.is_superuser)
        try:
            # username is None for the AbstractUser option
            # username does not exist for the AbstractBaseUser option
            self.assertIsNone(admin_user.username)
        except AttributeError:
            pass
        with self.assertRaises(ValueError):
            User.objects.create_superuser(email='', name='', password='foo')

    def test_user_login(self):
        self.user= User.objects.create_user(email='normal@user.com', name='normal', password='foo')
        response = self.client.post('/api/v1/token/',{'email': self.user.email,'password':'foo'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(response.data['refresh'])
        self.assertTrue(response.data['access'])
