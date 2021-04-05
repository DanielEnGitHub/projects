from django.urls import path
from . import views
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('/lista', views.listado, name="lista"),
    path('/nuevo', login_required(views.MascotaCreate.as_view()), name="nuevo"),
    path('/mascotaVer',login_required(views.MascotaList.as_view()), name="mascotaVer"),
    path('/mascotaEdit/<pk>',login_required(views.MascotaUpdate.as_view()), name="mascotaEdit"),
    path('/mascotaDelete/<pk>',login_required(views.MascotaDelete.as_view()), name="mascotaDelete"),
]
