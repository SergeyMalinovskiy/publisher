from rest_framework import serializers

from server.apps.books.models import Book
from server.apps.author.service import AuthorService


class BookModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'


class BookSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)

    name = serializers.CharField(required=True, max_length=255)
    registration_code = serializers.CharField(required=True, max_length=255)

    main_author = serializers.IntegerField(required=True, source='main_author.id')

    def save(self, **kwargs):

        author_id = self.validated_data.pop('main_author', {"id": None}).get('id')

        self.validated_data['main_author'] = AuthorService().try_to_get_author_or_except(author_id)

        return super().save(**kwargs)

    def create(self, validated_data):
        return Book.objects.create(**validated_data)

    def update(self, instance, validated_data):
        pass


class BookUpdateSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(required=False, max_length=255)
    registration_code = serializers.CharField(required=False, max_length=255)
    main_author = serializers.IntegerField(required=False, source="main_author.id")

    def validate(self, data):
        if not any(data.values()):
            raise serializers.ValidationError("Не передано не одно из полей для обновления")

        return data

    def create(self, validated_data):
        pass

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.registration_code = validated_data.get('registration_code', instance.registration_code)

        instance.main_author = validated_data.get('main_author', instance.main_author)

        instance.save()

        return instance

