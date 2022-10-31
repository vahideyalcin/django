from django.urls import include, path
from rest_framework import routers
from ogrenci.views import OgrencilerViewSet

router = routers.DefaultRouter(trailing_slash=True)

router.register(r"ogrenciler", OgrencilerViewSet, basename="ogrenci-viewset")

urlpatterns = [path("", include(router.urls))]
