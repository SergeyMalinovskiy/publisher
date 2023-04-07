# serializers
from rest_framework import serializers


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
