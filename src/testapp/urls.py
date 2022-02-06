from django.urls import path, include
from django.views.generic import TemplateView

app_name = 'test_app'

urlpatterns = [
    path('hello/1', TemplateView.as_view(template_name='hello1.html'), name='hello_1'),
    path('hello/2', TemplateView.as_view(template_name='hello2.html'), name='hello_2'),
    path('hello/3', TemplateView.as_view(template_name='hello3.html'), name='hello_3'),
    path('api/', include('testapp.api.urls'))
]
