"""View module for handling requests about magician services"""

import base64
from django.core.files.base import ContentFile
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework import status
from magicapi.models import MagicianService, Participant, Service
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.parsers import MultiPartParser, FormParser
from django.shortcuts import get_object_or_404
from rest_framework.exceptions import PermissionDenied


class MagicianServiceSerializer(serializers.ModelSerializer):
    """JSON serializer for magician services"""

    class Meta:
        model = MagicianService
        fields = (
            "id",
            "magician",
            "service",
            "description",
        )
        depth = 1

class MagicianServices(ViewSet):
    """Request handlers for magician services in the MagicianFinder Platform"""

    permission_classes = (IsAuthenticatedOrReadOnly,)

    def create(self, request):
        
        try:
            service = Service.objects.get(
                pk=request.data["service"]
            )
        except Service.DoesNotExist:
            return Response()

        magician = Participant.objects.get(user=request.auth.user)

        magicianservice_data = {
            "description": request.data["description"],
            "service": service,
            "magician": magician,
        }

        serializer = MagicianServiceSerializer(data=magicianservice_data, context={"request": request})

        if serializer.is_valid():

            new_magicianservice = MagicianService(
                description=serializer.validated_data["description"],
                service=service,
                magician=magician,
            )

            magician = Participant.objects.get(user=request.auth.user)
            new_magicianservice.magician = magician

            service = Service.objects.get(
                pk=request.data["service"]
            )

            new_magicianservice.service = service

            new_magicianservice.save()

            serializer = MagicianServiceSerializer(new_magicianservice, context={"request": request})

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):

        try:
            magicianservice = MagicianService.objects.get(pk=pk)
            serializer = MagicianServiceSerializer(magicianservice, context={"request": request})
            return Response(serializer.data)
        except Exception as ex:
            return HttpResponseServerError(ex)

    def update(self, request, pk=None):
        
        magicianservice = MagicianService.objects.get(pk=pk)
        participant = Participant.objects.get(user=request.auth.user)

        if magicianservice.magician_id == participant.id :

            magicianservice.description = request.data["description"]
            service = Service.objects.get(pk=request.data["service"])
            magicianservice.service = service
            magicianservice.save()

            return Response({}, status=status.HTTP_204_NO_CONTENT)
        
        else:
            raise PermissionDenied("You are not allowed to update this service.")
        


    def destroy(self, request, pk=None):

        try:
            magicianservice = MagicianService.objects.get(pk=pk)
            participant = Participant.objects.get(user=request.auth.user)

            if magicianservice.magician_id == participant.id :
        
                magicianservice.delete()

                return Response({}, status=status.HTTP_204_NO_CONTENT)
            
            else:
                raise PermissionDenied("You are not allowed to delete this service.")

        except MagicianService.DoesNotExist as ex:
            return Response({"message": ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

        except Exception as ex:
            return Response(
                {"message": ex.args[0]}, status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )

    # def list(self, request):
    #     """
    #     @api {GET} /products GET all products
    #     @apiName ListProducts
    #     @apiGroup Product

    #     @apiSuccess (200) {Object[]} products Array of products
    #     @apiSuccessExample {json} Success
    #         [
    #             {
    #                 "id": 101,
    #                 "url": "http://localhost:8000/products/101",
    #                 "name": "Kite",
    #                 "price": 14.99,
    #                 "number_sold": 0,
    #                 "description": "It flies high",
    #                 "quantity": 60,
    #                 "created_date": "2019-10-23",
    #                 "location": "Pittsburgh",
    #                 "image_path": null,
    #                 "average_rating": 0,
    #                 "category": {
    #                     "url": "http://localhost:8000/productcategories/6",
    #                     "name": "Games/Toys"
    #                 }
    #             }
    #         ]
    #     """
    #     products = Product.objects.all()

    #     # Support filtering by category and/or quantity
    #     category = self.request.query_params.get("category", None)
    #     quantity = self.request.query_params.get("quantity", None)
    #     order = self.request.query_params.get("order_by", None)
    #     direction = self.request.query_params.get("direction", None)
    #     store = self.request.query_params.get("store", None)
    #     number_sold = self.request.query_params.get("number_sold", None)
    #     min_price = self.request.query_params.get("min_price", None)
    #     name = self.request.query_params.get("name", None)
    #     location = self.request.query_params.get("location", None)
    #     customer = self.request.query_params.get("customer", None)

    #     if order is not None:
    #         order_filter = order

    #         if direction is not None:
    #             if direction == "desc":
    #                 order_filter = f"-{order}"

    #         products = products.order_by(order_filter)

    #     if category is not None:
    #         products = products.filter(category__id=category)

    #     if quantity is not None:
    #         products = products.order_by("-created_date")[: int(quantity)]

    #     if store is not None:
    #         found_store = Store.objects.get(pk=store)
    #         products = products.filter(customer=found_store.owner)

    #     if number_sold is not None:

    #         def sold_filter(product):
    #             if product.number_sold >= int(number_sold):
    #                 return True
    #             return False

    #         products = filter(sold_filter, products)

    #     if min_price is not None:
    #         products = products.filter(price__gte=min_price)

    #     if name is not None:
    #         products = products.filter(name__icontains=name)

    #     if location is not None:
    #         products = products.filter(location__icontains=location)

    #     if customer is not None:
    #         products = products.filter(customer=customer)

    #     serializer = ProductSerializer(
    #         products, many=True, context={"request": request}
    #     )
    #     return Response(serializer.data)
