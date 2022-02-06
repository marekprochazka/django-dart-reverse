from django.urls import get_resolver, URLResolver, URLPattern
from django_dart_reverse.utils.reverse_class import Reverse
from typing import Iterable


def collect_urls(patterns: list, names: list = None) -> Iterable[Reverse]:
    for pattern in patterns:
        new_list = names if names else []
        if isinstance(pattern, URLResolver):
            if pattern.app_name:
                new_list.append(pattern.app_name)
            collect_urls(pattern.url_patterns, new_list)
        else:
            # print(pattern.name)
            rvrs = Reverse(pattern, new_list)
            print(rvrs.name, rvrs.params, rvrs.path, rvrs.param_identifier)
            # yield Reverse(pattern, new_list)
