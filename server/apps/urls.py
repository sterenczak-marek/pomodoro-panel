from django.conf.urls import include, url

from rest_framework.routers import DefaultRouter

from .pomodoros.views import PomodoroViewSet
from .users.views import UserViewSet


router = DefaultRouter()
router.register(r'pomodoros', PomodoroViewSet, base_name='pomodoro')
router.register(r'users', UserViewSet)

urlpatterns = [
    url(r'^', include('apps.authentication.urls')),
    url(r'^', include(router.urls)),
]
