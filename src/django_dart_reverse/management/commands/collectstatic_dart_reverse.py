from django.core.management.base import BaseCommand
from django_dart_reverse.utils.collect_urls import collect_urls
from django.urls import get_resolver
from django.template import loader


class Command(BaseCommand):
    help = 'Creates .dart file with reverse dictionary'
    requires_system_checks = False

    def handle(self, *args, **kwargs):
        # collect_urls(get_resolver().url_patterns)
        print(loader.render_to_string('dart/dart_file.tpl', {
            'urls': [{'name': 'igor', 'params': ['jo'], 'path': 'jo/%{jo}'}],
            'identifiers': {
                'IGOR':'igor'
            }
        }))
