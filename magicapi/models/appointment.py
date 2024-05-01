from django.db import models
from .participant import Participant
from .magicianservice import MagicianService


class Appointment(models.Model):

    customer = models.ForeignKey(
        Participant,
        related_name="recommendations",
        on_delete=models.DO_NOTHING,
    )
    magicianService = models.ForeignKey(
        MagicianService,
        on_delete=models.DO_NOTHING,
    )
    date = models.DateField()