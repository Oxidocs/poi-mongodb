from django.contrib.auth.models import User, Group
from backend.models import Sexo, Perfil, Categoria, Subcategoria, Lugar, Empresa, Ruta, Circuito, Ranking, RankingEmpresa, Rol, Permiso, Galeria, Pais, Ciudad, Coordenada, Ranking, RankingEmpresa, Rol, Galeria
from rest_framework import viewsets
from api.serializers import UserSerializer, GroupSerializer, PerfilSerializer, CategoriaSerializer, SubcategoriaSerializer, PaisSerializer, CiudadSerializer, CiudadSerializer, LugarSerializer, EmpresaSerializer, RutaSerializer, CoordenadaSerializer, CircuitoSerializer, RankingSerializer, RankingEmpresaSerializer, RolSerializer, PermisoSerializer, PerfilSerializer, GaleriaSerializer


class UserViewSet(viewsets.ModelViewSet):
	queryset = User.objects.all().order_by('-date_joined')
	serializer_class = UserSerializer

class GroupViewSet(viewsets.ModelViewSet):
	queryset = Group.objects.all()
	serializer_class = GroupSerializer

class PerfilViewSet(viewsets.ModelViewSet):
	queryset = Perfil.objects.all()
	serializer_class = PerfilSerializer

class CategoriaViewSet(viewsets.ModelViewSet):
	queryset = Categoria.objects.all()
	serializer_class = CategoriaSerializer

class SubcategoriaViewSet(viewsets.ModelViewSet):
	queryset = Subcategoria.objects.all()
	serializer_class = SubcategoriaSerializer

class PaisViewSet(viewsets.ModelViewSet):
	queryset = Pais.objects.all()
	serializer_class = PaisSerializer

class CiudadViewSet(viewsets.ModelViewSet):
	queryset = Ciudad.objects.all()
	serializer_class = CiudadSerializer

class LugarViewSet(viewsets.ModelViewSet):
	queryset = Lugar.objects.all()
	serializer_class = LugarSerializer

class EmpresaViewSet(viewsets.ModelViewSet):
	queryset = Empresa.objects.all()
	serializer_class = EmpresaSerializer

class RutaViewSet(viewsets.ModelViewSet):
	queryset = Ruta.objects.all()
	serializer_class = RutaSerializer

class CircuitoViewSet(viewsets.ModelViewSet):
	queryset = Circuito.objects.all()
	serializer_class = CircuitoSerializer

class CoordenadaViewSet(viewsets.ModelViewSet):
	queryset = Coordenada.objects.all()
	serializer_class = CoordenadaSerializer

class RankingViewSet(viewsets.ModelViewSet):
	queryset = Ranking.objects.all()
	serializer_class = RankingSerializer

class RankingEmpresaViewSet(viewsets.ModelViewSet):
	queryset = RankingEmpresa.objects.all()
	serializer_class = RankingEmpresaSerializer

class RolViewSet(viewsets.ModelViewSet):
	queryset = Rol.objects.all()
	serializer_class = RolSerializer

class GaleriaViewSet(viewsets.ModelViewSet):
	queryset = Galeria.objects.all()
	serializer_class = GaleriaSerializer
