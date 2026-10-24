
from django.urls import path

from saludo.infrastructure.web.views import saludar


urlpatterns = [
    path("saludar/", saludar, name="saludar"),
]
