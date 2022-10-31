from statistics import mode
from unittest.util import _MAX_LENGTH
from django.db import models
import uuid
from sinif.rules import can_add_sinif



class Siniflar(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=200)
    numbers = models.IntegerField()
    female = models.IntegerField()
    male = models.IntegerField()
    department = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now=True)


class Meta:
        rules_permissions = {
            "view": can_add_sinif,
            "add": can_add_sinif,
            "change": can_add_sinif,
            "delete": can_add_sinif,
            "list": can_add_sinif,
        }