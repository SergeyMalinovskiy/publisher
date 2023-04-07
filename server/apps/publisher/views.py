from http import HTTPStatus

from django.http import Http404
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from server.apps.publisher.models import Publisher
from server.apps.publisher.serializers import PublisherModelSerializer, PublisherUpdateSerializer
from server.utils.decorators import TokenAuthenticatedOrReadOnly


@TokenAuthenticatedOrReadOnly()
# Create your views here.
class PublisherViewSet(ModelViewSet):
    queryset = Publisher.objects.all()
    serializer_class = PublisherModelSerializer

    def update(self, request, pk: int):
        try:
            publisher = Publisher.objects.get(pk=pk)
        except Publisher.DoesNotExist:
            raise Http404

        serializer = PublisherUpdateSerializer(publisher, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors, status=HTTPStatus.BAD_REQUEST)


