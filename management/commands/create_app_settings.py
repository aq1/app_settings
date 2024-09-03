import argparse

from django.core.management import BaseCommand

from app_settings.constants import create_default_app_settings


class Command(BaseCommand):
    def handle(self, *args, **options):
        create_default_app_settings()
