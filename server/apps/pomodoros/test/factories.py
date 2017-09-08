import factory

from ..models import Pomodoro

class PomodoroFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = Pomodoro
        django_get_or_create = ('user',)

    id = factory.Sequence(lambda n: uuid.uuid4())
