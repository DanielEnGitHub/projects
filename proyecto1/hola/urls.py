from django.urls import path
from . import views

urlpatterns = [
    path('', views.hola, name='hola'),
    path('usuarios/', views.usuarios, name='usuarios'),
    path('contabilidad/', views.contabilidad, name='contabilidad'),
    # path('<str:nombre>', views.saludo, name='saludo'),
    # path('<str:nombre>', views.saludoTemplate, name='saludoTemplate'),
    path('moneda/', views.moneda, name='moneda'),
]