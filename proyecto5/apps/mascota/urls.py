from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name=""),
    path('/nuevo', views.MascotaCreate.as_view(), name="nuevo"),
    path('/mascotaVer', views.MascotaList.as_view(), name="mascotaVer"),
    path('/mascotaEdit/<pk>', views.MascotaUpdate.as_view(), name="mascotaEdit"),
    path('/mascotaDelete/<pk>', views.MascotaDelete.as_view(), name="mascotaDelete"),
]
