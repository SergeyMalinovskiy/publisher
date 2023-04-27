from typing import Any

from rest_framework import serializers

from server.apps.publisher.models import Publisher
from server.utils.decorators import LeastOneFieldRequired


class PublisherModelSerializer(serializers.ModelSerializer):
    """Publisher in/out model serializer"""

    class Meta(type):
        model = Publisher
        fields = '__all__'


@LeastOneFieldRequired()
class PublisherUpdateSerializer(serializers.Serializer):
    """Publisher model update serializer (in)"""

    name = serializers.CharField(required=False, max_length=255)
    org_site = serializers.URLField(required=False, max_length=255)
    email = serializers.EmailField(required=False, max_length=255)

    def update(self, instance: Any, validated_data: Any) -> Any:
        """Update method"""
        instance.name = validated_data.get('name', instance.name)
        instance.org_site = validated_data.get('org_site', instance.org_site)
        instance.email = validated_data.get('email', instance.email)

        instance.save()

        return instance

