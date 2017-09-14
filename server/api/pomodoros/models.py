import uuid
from datetime import timedelta

from django.db import models
from django.conf import settings
from django.utils.translation import ugettext_lazy as _
from django.utils import timezone

from model_utils.models import TimeStampedModel


class Pomodoro(TimeStampedModel):

    DURATION = timedelta(minutes=25)

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='pomodoros')

    start_date = models.DateTimeField(_('Start date'), default=timezone.now)
    end_date = models.DateTimeField(_('End date'), null=True)

    def __str__(self):
        return "[{start_date} - {end_date}] {user}".format(
            start_date=self.start_date,
            end_date=self.end_date or "IN PROGRESS",
            user=self.user
        )
