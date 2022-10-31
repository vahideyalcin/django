from sinif.filters import SiniflarFilter
from sinif.models import Siniflar
from sinif.serializers import SiniflarSerializer
from django.apps import apps
from django.db import IntegrityError, transaction
from django.db.models import Q
from django.utils.translation import gettext_lazy as _
from django_auto_prefetching import AutoPrefetchViewSetMixin
from django_filters.rest_framework import DjangoFilterBackend
from drf_spectacular.utils import extend_schema
from jsonschema import ValidationError
from rest_framework import generics, status, viewsets
from rest_framework.decorators import action, parser_classes
from rest_framework.parsers import FileUploadParser
from rest_framework.response import Response
from rules.contrib.rest_framework import AutoPermissionViewSetMixin


class SiniflarViewSet(
    AutoPermissionViewSetMixin, AutoPrefetchViewSetMixin, viewsets.ModelViewSet
):
    queryset = Siniflar.objects.none()
    serializer_class = SiniflarSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = SiniflarFilter
    http_method_names = ["options", "get", "post", "put", "patch", "delete"]


    def get_queryset(self):
        # handle anonymous user case to aid in schema generation
        qs = Siniflar.objects.all()

        if self.request.user.is_active:
            queryset = qs
        elif self.request.user.is_superuser:
            queryset = qs
        else:
            return self.queryset.none()
        return queryset

    def list(self, request):
        """
        **List all Clinics requests related to the user.**

        User should be *authenticated* and have an *active* (is_active=True) account.

        **Roles required**: Staff and/or Admin

        """
        return super().list(request)

    def retrieve(self, request, *args, **kwargs):
        """
        **Get a specific Production Site request details.**

        User should be *authenticated* and have an *active* (is_active=True) account.

        **Roles required**: Staff and/or Admin

        """
        return super().retrieve(request, *args, **kwargs)

    def create(self, request):
        """
        **Create a specific production site.**

        User should be *authenticated* and have an *active* (is_active=True) account.

        **Roles required**: Staff and/or Admin

        **User employed by an active allowed organization**: Grid Operator
        """
        return super().create(request)

    def update(self, request, pk=None, *args, **kwargs):
        """
        **Upsert a specific production site.**

        User should be *authenticated* and have an *active* (is_active=True) account.

        **Note:** Production sites should be associated to a producer managed by the user.

        **Roles required**: Staff and/or Admin

        **User employed by an active allowed organization**: Grid Operator
        """
        return super().update(request, *args, **kwargs)

    def partial_update(self, request, *args, **kwargs):
        """
        **Update a specific production site.**

        User should be *authenticated* and have an *active* (is_active=True) account.

        ****Note:**** Object should be owned by the user's organization or retailer.

        **Roles required**: Staff and/or Admin

        **User employed by an active allowed organization**: Grid Operator
        """
        return super().partial_update(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        """
        **Delete a specific Production Site.**

        User should be *authenticated* and have an *active* (is_active=True) account.

        **Note:** Object should be owned by the user.

        **Roles required**: Admin

        **User employed by an active allowed organization**: Consumer or Retailer
        """
        return super().destroy(request, *args, **kwargs)
