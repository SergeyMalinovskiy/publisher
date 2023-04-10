# serializers
from rest_framework import serializers
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.views import APIView
from rest_framework_simplejwt.authentication import JWTAuthentication


class LeastOneFieldRequired(object):
    DEFAULT_ERROR_MESSAGE = "Least one field required!"

    @classmethod
    def validate(self, data):
        if not any(data.values()):
            raise serializers.ValidationError(self.DEFAULT_ERROR_MESSAGE)

        return data

    def __call__(self, cls: serializers.Serializer, ):
        setattr(cls, 'validate', self.validate)

        return cls


class TokenAuthenticatedOrReadOnly(object):
    def __call__(self, cls: APIView, *args, **kwargs):
        setattr(cls, 'authentication_classes', [JWTAuthentication])
        setattr(cls, 'permission_classes', [IsAuthenticatedOrReadOnly])

        return cls
