from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework import status
from magicapi.models import Participant


class ParticipantSerializer(serializers.HyperlinkedModelSerializer):
    """JSON serializer for Participants"""
    class Meta:
        model = Participant
        url = serializers.HyperlinkedIdentityField(
            view_name='Participant', lookup_field='id'
        )
        fields = ('id', 'url', 'user', 'ismagician')
        depth = 1


class Participants(ViewSet):

    def update(self, request, pk=None):
        """
        @api {PUT} /Participants/:id PUT changes to Participant profile
        @apiName UpdateParticipant
        @apiGroup Participant

        @apiHeader {String} Authorization Auth token
        @apiHeaderExample {String} Authorization
            Token 9ba45f09651c5b0c404f37a2d2572c026c146611

        @apiParam {id} id Participant Id to update
        @apiSuccessExample {json} Success
            HTTP/1.1 204 No Content
        """
        participant = Participant.objects.get(user=request.auth.user)
        participant.user.first_name = request.data["first_name"]
        participant.user.last_name = request.data["last_name"]
        participant.user.username = request.data["username"]
        participant.user.email = request.data["email"]
        participant.ismagician = request.data["ismagician"]
        participant.user.save()
        participant.save()

        return Response({}, status=status.HTTP_204_NO_CONTENT)