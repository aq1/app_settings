from django.db import models


class AppSetting(models.Model):
    name = models.CharField(
        verbose_name="Название",
        max_length=100,
        primary_key=True,
    )

    label = models.CharField(
        verbose_name="Описание",
        max_length=255,
    )

    value = models.JSONField(
        verbose_name="Значение",
        default=dict,
        help_text="in JSON format",
    )

    class Meta:
        verbose_name = "Настройка приложения"
        verbose_name_plural = "Настройки приложения"

    def __str__(self):
        return f"{self.name}"
