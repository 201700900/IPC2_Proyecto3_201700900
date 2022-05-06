from django.urls import path

from . import views

app_name = 'index'
urlpatterns = [
    path('', views.index, name='index'),
    path('cargar/', views.cargar, name='cargar'),
    path('solicitud/', views.getXML, name='solicitud'),
    path('prueba/', views.p, name='prueba'),
    path('prueba-mensaje/', views.prueba, name='prueba-mensaje'),
    path('pdf/', views.pdf, name='pdf'),
    path('reportes/', views.reportes, name='reportes'),
    path('reset/', views.reset, name='reset'),
    path('perfil/', views.perfil, name='perfil'),
    path('doc/', views.doc, name='doc'),








   
]