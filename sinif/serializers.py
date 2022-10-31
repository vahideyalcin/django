from django.apps import apps
from django.conf import settings
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator
from sinif.models import Siniflar


class SiniflarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Siniflar
        fields = ["id", "name", "female", "male", "department", "numbers", "created_at"]

        read_only_fields = [
            "id",
            "created_at",
        ]
        extra_kwargs = {"department": {"required": True}}
