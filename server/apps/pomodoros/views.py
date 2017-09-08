from rest_framework import viewsets, mixins
from rest_framework.permissions import AllowAny

from .models import Pomodoro
from .serializers import CreatePomodoroSerializer, PomodoroSerializer


class PomodoroViewSet(viewsets.ModelViewSet):
    """
    Creates, Updates, and retrives Pomodoros
    """

    queryset = Pomodoro.objects.none()
    serializer_class = PomodoroSerializer

    def get_queryset(self):
        if self.request.user.is_authenticated():
            return self.request.user.pomodoros.all()

        return Pomodoro.objects.none()

    def create(self, request, *args, **kwargs):
        self.serializer_class = CreatePomodoroSerializer
        return super(PomodoroViewSet, self).create(request, *args, **kwargs)
