from typing import Dict, Any

from rest_framework import serializers

from server.apps.subscribes.models import Subscribe


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
