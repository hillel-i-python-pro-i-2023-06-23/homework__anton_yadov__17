from django.core.management.base import BaseCommand

from apps.contacts.services.create_admin import create_admin


class Command(BaseCommand):
    def handle(self, *args, **options):
        create_admin()
