from rest_framework import serializers

from .models import Break


class BreakSerializer(serializers.ModelSerializer):

    class Meta:
        model = Break
        fields = ('id', 'user', 'start_date', 'end_date',)


class CreateBreakSerializer(serializers.ModelSerializer):

    def create(self, validated_data):
        user = self.context['request'].user
        return Break.objects.create(user=user)

    class Meta:
        model = Break
        fields = []
        read_only_fields = ['start_date']
