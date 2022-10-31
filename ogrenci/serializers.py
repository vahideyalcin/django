from django.apps import apps
from django.conf import settings
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator
from ogrenci.models import Ogrenciler


class OgrencilerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ogrenciler
        fields = ["id", "name", "gender", "age", "gano", "created_at"]

        read_only_fields = [
            "id",
            "created_at",
        ]
        extra_kwargs = {"name": {"required": True}}
