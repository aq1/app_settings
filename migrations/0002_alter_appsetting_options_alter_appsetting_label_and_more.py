# Generated by Django 5.1 on 2024-08-31 11:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("app_settings", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="appsetting",
            options={
                "verbose_name": "Настройка приложения",
                "verbose_name_plural": "Настройки приложения",
            },
        ),
        migrations.AlterField(
            model_name="appsetting",
            name="label",
            field=models.CharField(max_length=255, verbose_name="Описание"),
        ),
        migrations.AlterField(
            model_name="appsetting",
            name="name",
            field=models.CharField(
                max_length=100,
                primary_key=True,
                serialize=False,
                verbose_name="Название",
            ),
        ),
        migrations.AlterField(
            model_name="appsetting",
            name="value",
            field=models.JSONField(
                default=dict, help_text="in JSON format", verbose_name="Значение"
            ),
        ),
    ]
