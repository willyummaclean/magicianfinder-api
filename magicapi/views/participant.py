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

class ParticipantWithUserIdSerializer(serializers.HyperlinkedModelSerializer):
    """JSON serializer for Participants"""
    class Meta:
        model = Participant
        url = serializers.HyperlinkedIdentityField(
            view_name='Participant', lookup_field='id'
        )
        fields = ('id', 'url', 'user_id', 'ismagician')
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
    
    def list(self, request):
        """Handle GET requests to user resource"""
        participants = Participant.objects.all()

        ismagician = self.request.query_params.get("ismagician", None)
        if ismagician is not None:
            participants = participants.filter(ismagician=True)

        serializer = ParticipantSerializer(participants, many=True, context={"request": request})
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        """Handle GET requests for single customer
        Purpose: Allow a user to communicate with the MagicianFinder database to retrieve  one user
        Methods:  GET
        Returns:
            Response -- JSON serialized customer instance
        """
        try:
            participant = Participant.objects.get(pk=pk)
            serializer = ParticipantSerializer(participant, context={"request": request})
            return Response(serializer.data)
        except Exception as ex:
            return HttpResponseServerError(ex)