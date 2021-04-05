from django.urls import path, include
from . import views

urlpatterns = [
    path('/registrar', views.RegistroUsuario.as_view(), name="registrar"),
]