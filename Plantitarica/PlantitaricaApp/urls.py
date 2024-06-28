
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('agregar-plantas/', views.agregar_plantas, name='agregar_plantas'),
    path('agregar-maceteros/', views.agregar_maceteros, name='agregar_maceteros'),
    path('agregar-insumos/', views.agregar_insumos, name='agregar_insumos'),
    path('btnAgregarPlantas', views.btnAgregarPlantas, name='btnAgregarPlantas'),
    path('btnAgregarMaceteros', views.btnAgregarMaceteros, name='btnAgregarMaceteros'),
    path('btnAgregarInsumos', views.btnAgregarInsumos, name='btnAgregarInsumos'),
    path('Productos/', views.Productos, name='Productos'),
    path('Maceteros/', views.PMaceteros, name='Maceteros'),
    path('Insumos/', views.PInsumos, name='Insumos'),
    path('AcercaDe/', views.AcercaDe, name='AcercaDe'),
    path('Contacto/', views.Contacto, name='Contacto'),

]