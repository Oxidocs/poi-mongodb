from django.conf.urls import url, include
from rest_framework import routers
from api import views, urls_auth

router = routers.DefaultRouter()
router.register(r'usuarios', views.UserViewSet)
router.register(r'grupos', views.GroupViewSet)
router.register(r'perfiles', views.PerfilViewSet)
router.register(r'rutas', views.RutaViewSet)
router.register(r'circuitos', views.CircuitoViewSet)
router.register(r'categorias', views.CategoriaViewSet)
router.register(r'lugares', views.LugarViewSet)
router.register(r'empresas', views.EmpresaViewSet)
# router.register(r'sexos', views.SexoViewSet)
router.register(r'subcategorias', views.SubcategoriaViewSet)

router.register(r'paises', views.PaisViewSet)
router.register(r'ciudades', views.CiudadViewSet)
router.register(r'coordenadas', views.CoordenadaViewSet)
router.register(r'rankings', views.RankingViewSet)
router.register(r'rankings_empresas', views.RankingEmpresaViewSet)
router.register(r'roles', views.RolViewSet)
router.register(r'galerias', views.GaleriaViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^', include(urls_auth))
]
