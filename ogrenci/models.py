from statistics import mode
from unittest.util import _MAX_LENGTH
from django.db import models
import uuid
from ogrenci.rules import can_add_ogrenci

# Create your models here.


class Ogrenciler(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=200)
    gano = models.FloatField()
    gender = models.CharField(max_length=200)
    age = models.IntegerField()
    sinif = models.ForeignKey(
        "sinif.Siniflar",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )
    created_at = models.DateTimeField(auto_now=True)

class Meta:
    rules_permissions = {
        "view": can_add_ogrenci,
        "add": can_add_ogrenci,
        "change": can_add_ogrenci,
        "delete": can_add_ogrenci,
        "list": can_add_ogrenci,
    }