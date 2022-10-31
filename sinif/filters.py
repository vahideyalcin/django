from django_filters import IsoDateTimeFilter, OrderingFilter
from django_filters import rest_framework as filters
from sinif.models import Siniflar


class SiniflarFilter(filters.FilterSet):

    order_by = OrderingFilter(
        # tuple-mapping retains order
        fields=(("created_at", "created_at"))
    )

    class Meta:
        model = Siniflar
        fields = [
            "id",
            "name",
            "female",
            "male",
            "department",
            "numbers",
            "created_at",
        ]
