from django.core.management.base import BaseCommand
from django.db import connection

class Command(BaseCommand):
    help = 'Drops the events_event table'

    def handle(self, *args, **kwargs):
        with connection.cursor() as cursor:
            cursor.execute("DROP TABLE IF EXISTS events_event;")
        self.stdout.write(self.style.SUCCESS('Successfully dropped events_event table'))
