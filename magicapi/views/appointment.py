
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework import status
from magicapi.models import MagicianService, Participant, Service, Appointment
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.exceptions import PermissionDenied
from magicapi.views.magicianservice import MagicianServiceSerializer
from magicapi.views.participant import ParticipantSerializer
from django.http import HttpResponseServerError

class AppointmentSerializer(serializers.ModelSerializer):
    """JSON serializer for magician services"""

    # magicianService = MagicianServiceSerializer(many=False)
    # customer = ParticipantSerializer(many=False)

    class Meta:
        model = Appointment
        fields = (
            "date",
            "customer",
            "magicianService"
        )
        depth = 1

class Appointments(ViewSet):
    """Request handlers for appointments in the MagicianFinder Platform"""

    permission_classes = (IsAuthenticatedOrReadOnly,)

    def create(self, request):
        
        try:
            magicianService = MagicianService.objects.get(
                pk=request.data["magicianService"]
            )
        except MagicianService.DoesNotExist:
            return Response()

        customer = Participant.objects.get(user=request.auth.user)

        appointment_data = {
            "date": request.data["date"],
            "magicianService": magicianService,
            "customer": customer,
        }

        serializer = AppointmentSerializer(data=appointment_data, context={"request": request})

        if serializer.is_valid():

            new_appointment = Appointment(
                date=serializer.validated_data["date"],
                magicianService=magicianService,
                customer=customer,
            )

            customer = Participant.objects.get(user=request.auth.user)
            new_appointment.customer = customer

            magicianService = MagicianService.objects.get(
                pk=request.data["magicianService"]
            )

            new_appointment.magicianService = magicianService

            new_appointment.save()

            serializer = AppointmentSerializer(new_appointment, context={"request": request})

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        

    def retrieve(self, request, pk=None):

        try:
            appointment = Appointment.objects.get(pk=pk)
            serializer = AppointmentSerializer(appointment, context={"request": request})
            return Response(serializer.data)
        except Exception as ex:
            return HttpResponseServerError(ex)

    def destroy(self, request, pk=None):

        try:
            appointment = Appointment.objects.get(pk=pk)
            customer = Participant.objects.get(user=request.auth.user)

            if appointment.customer_id == customer.id :
        
                appointment.delete()

                return Response({}, status=status.HTTP_204_NO_CONTENT)
            
            else:
                raise PermissionDenied("You are not allowed to delete this service.")

        except Appointment.DoesNotExist as ex:
            return Response({"message": ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

        except Exception as ex:
            return Response(
                {"message": ex.args[0]}, status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )