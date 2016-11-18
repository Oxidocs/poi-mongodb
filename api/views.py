from django.contrib.auth.models import User, Group
from backend.models import Rutas, Perfiles, Lugares, Categorias
from rest_framework import viewsets
from api.serializers import UserSerializer, GroupSerializer, RutasSerializer, PerfilesSerializer, LugaresSerializer, CategoriasSerializer


class UserViewSet(viewsets.ModelViewSet):
	queryset = User.objects.all().order_by('-date_joined')
	serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
	queryset = Group.objects.all()
	serializer_class = GroupSerializer

class PerfilesViewSet(viewsets.ModelViewSet):
	queryset = Perfiles.objects.all()
	serializer_class = PerfilesSerializer

class RutasViewSet(viewsets.ModelViewSet):
	queryset = Rutas.objects.all()
	serializer_class = RutasSerializer

class CategoriasViewSet(viewsets.ModelViewSet):
	queryset = Categorias.objects.all()
	serializer_class = CategoriasSerializer

class LugaresViewSet(viewsets.ModelViewSet):
	queryset = Lugares.objects.all()
	serializer_class = LugaresSerializer