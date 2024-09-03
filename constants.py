from django.conf import settings

from app_settings.models import AppSetting


def create_default_app_settings():
    for key, value in settings.DEFAULT_APP_SETTINGS.items():
        _, created = AppSetting.objects.get_or_create(
            name=key,
            defaults=dict(
                label=key,
                value=value,
            ),
        )

        if created:
            print(f"{key} created")
