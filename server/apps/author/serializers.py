from rest_framework import serializers

from server.apps.author.models import Author
from server.utils.decorators import LeastOneFieldRequired


class AuthorModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = "__all__"


class AuthorSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)

    surname = serializers.CharField(required=True, allow_blank=True, max_length=255)
    name = serializers.CharField(required=True, allow_blank=True, max_length=255)

    license_code = serializers.CharField(required=False)

    def create(self, validated_data):
        return Author.objects.create(**validated_data)

    def update(self, instance, validated_data):
        pass


@LeastOneFieldRequired()
class AuthorUpdateSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)

    surname = serializers.CharField(required=False, allow_blank=True, max_length=255)
    name = serializers.CharField(required=False, allow_blank=True, max_length=255)
    license_code = serializers.CharField(required=False)

    def create(self, validated_data):
        pass

    def update(self, instance, validated_data):
        instance.surname = validated_data.get('surname', instance.surname)
        instance.name = validated_data.get('name', instance.name)
        instance.license_code = validated_data.get('license_code', instance.license_code)

        instance.save()

        return instance

