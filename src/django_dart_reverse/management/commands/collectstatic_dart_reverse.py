from typing import List
from django.core.management.base import BaseCommand
from django_dart_reverse.utils.collect_urls import collect_urls
from django.urls import get_resolver
from django.template import loader

from django_dart_reverse.utils.reverse_class import Reverse


class Command(BaseCommand):
    help = 'Creates .dart file with reverse dictionary'
    requires_system_checks = False

    def handle(self, *args, **kwargs):
        urls = list()
        for value in collect_urls(get_resolver().url_patterns):
            urls.append(value)

        print(loader.render_to_string('dart/dart_file.tpl', dict(urls=urls)))

    def __remove_duplicates(self, urls: List[Reverse]) -> List[Reverse]:
        pass
