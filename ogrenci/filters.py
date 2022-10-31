from django_filters import IsoDateTimeFilter, OrderingFilter
from django_filters import rest_framework as filters
from ogrenci.models import Ogrenciler


class OgrencilerFilter(filters.FilterSet):

    order_by = OrderingFilter(
        # tuple-mapping retains order
        fields=(("created_at", "created_at"))
    )

    class Meta:
        model = Ogrenciler
        fields = ["id", "name", "gender", "age", "gano", "created_at"]
