# vim: set fileencoding=utf-8 :
from django.contrib import admin
from ogrenci import models
from . import models


class OgrenciAdmin(admin.ModelAdmin):

    list_display = ("id", "name", "gender", "age", "gano", "created_at")
    list_filter = ("name",)
    date_hierarchy = "created_at"
    search_fields = (
        "id",
        "name",
    )
    ordering = ("-created_at",)


admin.site.register(models.Ogrenciler, OgrenciAdmin)
