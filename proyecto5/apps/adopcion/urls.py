from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('solicitud/solicitudVer', views.SolicitudList.as_view(), name="solicitudVer"),
    path('solicitud/nuevo', views.SolicitudCreate.as_view(), name="solicitud_crear"),
]
