from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'^home/', views.Index, name='index'),
	url(r'^editar_perfil/', views.editarPerfil, name='editar-perfil'),
	# url(r'^post/(?P<pk>[0-9]+)/$', views.perfil_detail),
	url(r'^destinos/', views.Destinos, name='destinos'),
	url(r'^servicios/', views.Servicios, name='servicios'),
	url(r'^productos/', views.Productos, name='productos'),
	url(r'^circuitos/', views.Circuitos, name='circuitos'),
	url(r'^rutas/', views.Rutas, name='rutas'),
	url(r'^estadisticas/', views.Estadisticas, name='estadisticas'),
	url(r'^informes/', views.Informes, name='informes'),
	url(r'^calendarios/', views.Calendarios, name='calendarios'),
	url(r'^get_perfil/', views.getPerfil, name='get-perfil'),
	url(r'^guardar_lugar/', views.saveLugar, name='guardar-lugar'),
	url(r'^mostrar_lugar/', views.getLugar, name='mostrar-lugar'),
]