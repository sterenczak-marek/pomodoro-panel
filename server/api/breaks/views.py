from rest_framework import viewsets, mixins
from rest_framework.permissions import AllowAny

from .models import Break
from .serializers import CreateBreakSerializer, BreakSerializer


class BreakViewSet(viewsets.ModelViewSet):
    """
    Creates, Updates, and retrives Breaks
    """

    queryset = Break.objects.none()
    serializer_class = BreakSerializer

    def get_queryset(self):
        if self.request.user.is_authenticated():
            return self.request.user.pomodoros.all()

        return Break.objects.none()

    def create(self, request, *args, **kwargs):
        self.serializer_class = CreateBreakSerializer
        return super(BreakViewSet, self).create(request, *args, **kwargs)
