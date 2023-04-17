from urllib.request import Request

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from server.apps.subscribes.models import Subscribe
from server.apps.subscribes.serializers import SubscribeSerializer, CreateSubscribeSerializer


class SubscribesAPIView(APIView):
    """Subscribes API View class"""

    def post(self, request: Request, event: str) -> Response:
        """Create new subscribe"""
        serializer = CreateSubscribeSerializer(data=request.data)

        print(request.data)

        if serializer.is_valid():
            serializer.save()
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
