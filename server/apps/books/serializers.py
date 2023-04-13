from typing import Any, Dict

from rest_framework import serializers

from server.apps.books.models import Book
from server.apps.author.service import AuthorService
from server.utils.decorators import LeastOneFieldRequired


class BookSerializer(serializers.Serializer):
    """
    Book serializer for create or list methods
    """

    id = serializers.IntegerField(read_only=True)

    name = serializers.CharField(required=True, max_length=255)
    registration_code = serializers.CharField(required=True, max_length=255)

    main_author = serializers.IntegerField(
        required=True,
        source='main_author.id',
    )

    def save(self, **kwargs: Dict) -> Any:
        """
        Save book instance.
        """
        author = self.validated_data.pop('main_author', {'id': None})
        author_id = author.get('id')

        main_author = AuthorService().try_to_get_author_or_except(author_id)

        self.validated_data['main_author'] = main_author

        return super().save(**kwargs)

    def create(self, validated_data: Any) -> Book:
        """Create book object in DB."""
        return Book.objects.create(**validated_data)

    def update(self, instance: Any, validated_data: Any) -> Any:
        """pass."""


@LeastOneFieldRequired()
class BookUpdateSerializer(serializers.Serializer):
    """Responses for update method."""

    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(required=False, max_length=255)
    registration_code = serializers.CharField(required=False, max_length=255)

    main_author = serializers.IntegerField(
        required=False,
        source='main_author.id',
    )

    def create(self, validated_data: Any) -> Any:
        """pass."""

    def update(self, instance: Any, validated_data: Dict) -> Any:
        """Update book model."""
        instance.name = validated_data.get('name', instance.name)
        instance.registration_code = validated_data.get(
            'registration_code',
            instance.registration_code,
        )

        instance.main_author = validated_data.get(
            'main_author',
            instance.main_author,
        )

        instance.save()

        return instance

