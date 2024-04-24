from django.db import models
from .participant import Participant
from .service import Service


class MagicianService(models.Model):

    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    magician = models.ForeignKey(Participant, on_delete=models.CASCADE)
    description = models.CharField(max_length=55)