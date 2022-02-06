from django.urls import get_resolver, URLResolver, URLPattern


def collect_urls(patterns: list, names: list = None) -> None:
    for pattern in patterns:
        new_list = names if names else []
        if isinstance(pattern, URLResolver):
            if pattern.app_name:
                new_list.append(pattern.app_name)
            collect_urls(pattern.url_patterns, new_list)
        else:
            print(f'{new_list}{pattern.name} -> {pattern.pattern}')
