from django.urls import path
from . import views
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('/solicitud/solicitudVer',login_required(views.SolicitudList.as_view()), name="solicitudVer"),
    path('/solicitud/nuevo', login_required(views.SolicitudCreate.as_view()), name="solicitud_crear"),
    path('/solicitud/solicitudEdit/<pk>',login_required(views.SolicitudUpdate.as_view()), name="solicitudEdit"),
    path('/solicitud/solicitudDelete/<pk>',login_required(views.SolicitudDelete.as_view()), name="solicitudDelete"),
]
