from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from apps.users.test.factories import UserFactory
from ..models import Pomodoro

class PomodoroTests(APITestCase):

    def setUp(self):
        user = UserFactory()
        self.client.force_authenticate(user)

    def test_create_pomodoro(self):

        url = reverse('api:pomodoro-list')
        data = {}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Pomodoro.objects.count(), 1)

        created_pomodoro = Pomodoro.objects.get()
        self.assertEqual(created_pomodoro.created.replace(microsecond=0), created_pomodoro.start_date.replace(microsecond=0))
        self.assertEqual(created_pomodoro.end_date, None)
