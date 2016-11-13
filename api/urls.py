from django.conf.urls import url, include
from rest_framework import routers
from api import views, urls_auth

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)
router.register(r'rutas', views.RutasViewSet)
router.register(r'perfiles', views.PerfilesViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^', include(urls_auth))
]
