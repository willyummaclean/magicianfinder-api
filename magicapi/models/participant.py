from django.db import models
from django.contrib.auth.models import User


class Participant(models.Model):

    user = models.OneToOneField(
        User,
        on_delete=models.DO_NOTHING,
    )
    ismagician = models.BooleanField()

