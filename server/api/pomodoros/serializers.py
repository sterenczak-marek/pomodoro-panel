from rest_framework import serializers

from .models import Pomodoro


class PomodoroSerializer(serializers.ModelSerializer):

    class Meta:
        model = Pomodoro
        fields = ('id', 'user', 'start_date', 'end_date',)


class CreatePomodoroSerializer(serializers.ModelSerializer):

    def create(self, validated_data):
        user = self.context['request'].user
        return Pomodoro.objects.create(user=user)

    class Meta:
        model = Pomodoro
        fields = []
        read_only_fields = ['start_date']
