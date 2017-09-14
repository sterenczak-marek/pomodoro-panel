from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from api.users.test.factories import UserFactory
from ..models import Break


class BreakTests(APITestCase):

    def setUp(self):
        user = UserFactory()
        self.client.force_authenticate(user)

    def test_create_pomodoro(self):

        url = reverse('api:break-list')
        data = {}

        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Break.objects.count(), 1)

        created_break = Break.objects.get()
        self.assertEqual(created_break.created.replace(microsecond=0), created_break.start_date.replace(microsecond=0))
        self.assertEqual(created_break.end_date, None)

    def test_anonymous_user(self):

        self.client.logout()

        url = reverse('api:break-list')
        data = {}

        response = self.client.get(url, data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

