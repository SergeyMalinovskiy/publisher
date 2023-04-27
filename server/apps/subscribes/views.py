from urllib.request import Request

from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.authentication import JWTAuthentication

from server.apps.subscribes.models import Subscribe, Event
from server.apps.subscribes.serializers import (
    SubscribeSerializer,
    CreateSubscribeSerializer,
    EventSerializer,
)
from server.apps.subscribes.tasks import send_subscribe_notification


class SubscribesAPIView(APIView):
    """Subscribes API View class"""

    authentication_classes = (JWTAuthentication,)
    permission_classes = (IsAuthenticated, )

    def post(self, request: Request, event: str) -> Response:
        """Create new subscribe"""
        serializer = CreateSubscribeSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()

            # TODO: Необходимо добавить задачу для отправки уведомления о созданной подписке
            # send_subscribe_notification.delay()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request: Request) -> Response:
        """List of subscribes"""
        subscribes = Subscribe.objects.all()

        serializer = SubscribeSerializer(subscribes, many=True)

        return Response(data=serializer.data)

    def delete(self, request: Request) -> Response:
        """Delete subscribe"""
        return Response()
