from django.core.management.base import BaseCommand
from django_dart_reverse.utils.collect_urls import collect_urls
from django.urls import get_resolver


class Command(BaseCommand):
    help = 'Creates .dart file with reverse dictionary'
    requires_system_checks = False

    def handle(self, *args, **kwargs):
        collect_urls(get_resolver().url_patterns)
