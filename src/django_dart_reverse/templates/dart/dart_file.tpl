class Reverse {
    static final Map urls = {
    {% for url in urls %}
    {{url.name}}:({% for param in url.params %}String {{param}},{% endfor %}) => {{url.path}},
    {% endfor %}
    };
    {% for key, value in identifiers.items %}
    static const String {{key}} = {{value}};
    {% endfor %}
}