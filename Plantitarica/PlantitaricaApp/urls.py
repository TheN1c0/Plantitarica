
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('agregar-producto/', views.agregar_producto, name='agregar_producto'),
    path('btnAgregarProduc', views.btnAgregarProduc, name='btnAgregarProduc'),
    path('Productos/', views.Productos, name='Productos'),
    path('Maceteros/', views.PMaceteros, name='Maceteros'),
    path('Insumos/', views.PInsumos, name='Insumos'),
    path('AcercaDe/', views.AcercaDe, name='AcercaDe'),
    path('Contacto/', views.Contacto, name='Contacto'),

]