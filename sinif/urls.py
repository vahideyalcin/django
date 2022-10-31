from django.urls import include, path
from rest_framework import routers
from sinif.views import SiniflarViewSet

router = routers.DefaultRouter(trailing_slash=True)

router.register(r"siniflar", SiniflarViewSet, basename="sinif-viewset")

urlpatterns = [path("", include(router.urls))]
