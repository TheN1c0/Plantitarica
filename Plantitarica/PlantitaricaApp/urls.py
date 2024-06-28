
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('agregar-producto/', views.agregar_producto, name='agregar_producto'),
    path('btnAgregarProduc', views.btnAgregarProduc, name='btnAgregarProduc'),
]