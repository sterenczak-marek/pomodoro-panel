from django.test import TestCase

from apps.users.test.factories import UserFactory


class AuthTokenTestCase(TestCase):

    def setUp(self):
        self.user = UserFactory()

    def test_new_users_get_auth_token(self):

        self.user.auth_token
