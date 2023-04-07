from rest_framework import serializers

import server.utils.decorators
from server.apps.publisher.models import Publisher
from server.utils.decorators import LeastOneFieldRequired


class PublisherModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Publisher
        fields = "__all__"


@LeastOneFieldRequired()
class PublisherUpdateSerializer(serializers.Serializer):
    name = serializers.CharField(required=False, max_length=255)
    org_site = serializers.URLField(required=False, max_length=255)
    email = serializers.EmailField(required=False, max_length=255)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.org_site = validated_data.get('org_site', instance.org_site)
        instance.email = validated_data.get('email', instance.email)

        instance.save()

        return instance

