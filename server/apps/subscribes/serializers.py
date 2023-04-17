from rest_framework import serializers

from server.apps.subscribes.models import Subscribe, Event


class SubscribeSerializer(serializers.ModelSerializer):
    """Data serializer for subscribe model"""

    class Meta(type):
        model = Subscribe
        fields = '__all__'


class CreateSubscribeSerializer(serializers.ModelSerializer):
    """Create subscribe serializer"""

    class Meta(type):
        model = Subscribe
        fields = ['event', 'valid_until_date']


class EventSerializer(serializers.ModelSerializer):
    """Event serializer"""

    class Meta(type):
        model = Event
        field = '__all__'
