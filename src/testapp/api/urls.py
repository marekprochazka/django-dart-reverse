from django.urls import path
from django.views.generic import TemplateView

app_name = 'test_app_api'

urlpatterns = [
    path('test/3', TemplateView.as_view(template_name='hello3.html'), name='hello_3'),
    path('test/<str:name>/<str:surname>', TemplateView.as_view(template_name='hello3.html'), name='hello_with_params'),
]
