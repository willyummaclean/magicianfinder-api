from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework import status
from magicapi.models import Service
from rest_framework.permissions import IsAuthenticatedOrReadOnly


class ServiceSerializer(serializers.HyperlinkedModelSerializer):
    """JSON serializer for product category"""

    class Meta:
        model = Service
        url = serializers.HyperlinkedIdentityField(
            view_name="service", lookup_field="id"
        )
        fields = ("id", "url", "name")


class Services(ViewSet):
    """Services"""

    permission_classes = (IsAuthenticatedOrReadOnly,)

    def create(self, request):
        """Handle POST operations

        Returns:
            Response -- JSON serialized service instance
        """
        new_service = Service()
        new_service.name = request.data["name"]
        new_service.save()

        serializer = ServiceSerializer(
            new_service, context={"request": request}
        )

        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def retrieve(self, request, pk=None):
        """Handle GET requests for single category"""
        try:
            service = Service.objects.get(pk=pk)
            serializer = ServiceSerializer(
                service, context={"request": request}
            )
            return Response(serializer.data)
        except Exception as ex:
            return HttpResponseServerError(ex)

    def list(self, request):
        """Handle GET requests to ProductCategory resource"""
        service = Service.objects.all()

        serializer = ServiceSerializer(
           service, many=True, context={"request": request}
        )
        return Response(serializer.data)