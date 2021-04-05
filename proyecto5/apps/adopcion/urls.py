from django.urls import path
from . import views

urlpatterns = [
    path('/solicitudVer', views.SolicitudList.as_view(), name="solicitudVer"),
]
