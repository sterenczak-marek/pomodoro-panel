from django.conf.urls import include, url

from rest_framework.routers import SimpleRouter

from .pomodoros.views import PomodoroViewSet
from .breaks.views import BreakViewSet
from .users.views import UserViewSet


router = SimpleRouter()
router.register(r'pomodoros', PomodoroViewSet, base_name='pomodoro')
router.register(r'breaks', BreakViewSet)
router.register(r'users', UserViewSet)


urlpatterns = [
    url(r'^auth/', include('rest_auth.urls')),
    url(r'^', include(router.urls)),
]
