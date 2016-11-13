from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'^home/', views.Index, name='index'),
	url(r'^destinos/', views.Destinos, name='destinos'),
	url(r'^servicios/', views.Servicios, name='servicios'),
	url(r'^productos/', views.Productos, name='productos'),
	url(r'^circuitos/', views.Circuitos, name='circuitos'),
	url(r'^rutas/', views.Rutas, name='rutas'),
	url(r'^estadisticas/', views.Estadisticas, name='estadisticas'),
	url(r'^informes/', views.Informes, name='informes'),
	url(r'^calendarios/', views.Calendarios, name='calendarios'),
	url(r'^get_perfil/', views.getPerfil, name='get-perfil'),
]