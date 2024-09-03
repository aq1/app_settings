from .models import AppSetting


async def get_app_setting(name: str):
    return (await AppSetting.objects.aget(name=name)).value


app_settings = get_app_setting
