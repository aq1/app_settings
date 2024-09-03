from django.contrib import admin
from django.db import models
from django_json_widget.widgets import JSONEditorWidget

from ..models import AppSetting


@admin.register(AppSetting)
class AppSettingAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "label",
    )

    ordering = ("name",)

    formfield_overrides = {
        models.JSONField: {"widget": JSONEditorWidget(mode="code")},
    }
