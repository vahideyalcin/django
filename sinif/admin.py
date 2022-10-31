# vim: set fileencoding=utf-8 :
from django.contrib import admin
from sinif import models
from . import models


class SiniflarAdmin(admin.ModelAdmin):

    list_display = (
        "id",
        "name",
        "female",
        "male",
        "department",
        "numbers",
        "created_at",
    )
    list_filter = (
        "name",
        "department",
        "numbers",
    )
    date_hierarchy = "created_at"
    search_fields = (
        "id",
        "name",
    )
    ordering = ("-created_at",)


admin.site.register(models.Siniflar, SiniflarAdmin)
