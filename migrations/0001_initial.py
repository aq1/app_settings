# Generated by Django 5.1 on 2024-09-03 10:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="AppSetting",
            fields=[
                (
                    "name",
                    models.CharField(
                        max_length=100,
                        primary_key=True,
                        serialize=False,
                        verbose_name="Название",
                    ),
                ),
                ("label", models.CharField(max_length=255, verbose_name="Описание")),
                (
                    "value",
                    models.JSONField(
                        default=dict,
                        help_text="in JSON format",
                        verbose_name="Значение",
                    ),
                ),
            ],
            options={
                "verbose_name": "Настройка приложения",
                "verbose_name_plural": "Настройки приложения",
            },
        ),
    ]
