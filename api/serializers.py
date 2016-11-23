from django.contrib.auth.models import User, Group
from rest_framework import serializers
from backend.models import Sexo, Perfil, Categoria, Subcategoria, Lugar, Empresa, Ruta, Circuito, Ranking, RankingEmpresa, Rol, Permiso, Galeria, Pais, Ciudad, Coordenada
    

class UserSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = User
		fields = ('url', 'username', 'email')


class GroupSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Group
		fields = ('url', 'name')

class PerfilSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Perfil
		fields = ('url', 'usuario', 'sexo', 'emails', 'telefonos', 'fecha_de_nac', 'image')

class CategoriaSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Categoria
		fields = ('url', 'nombre', 'descripcion')

class SubcategoriaSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Subcategoria
		fields = ('url', 'nombre', 'descripcion', 'categoria')

class PaisSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Pais
		fields = ('url', 'nombre')

class CiudadSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Ciudad
		fields = ('url', 'nombre', 'pais')

class LugarSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Lugar
		fields = ('url', 'nombre', 'descripcion', 'categoria', 'ciudad', 'location', 'objects', 'direccion', 'icono', 'portada', 'sitio_web', 'redes_sociales', 'fecha_de_creacion', 'tags')

class EmpresaSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Empresa
		fields = ('url', 'nombre', 'descripcion', 'categoria', 'ciudad', 'objects', 'direccion', 'icono', 'portada', 'sitio_web', 'redes_sociales', 'fecha_de_creacion', 'tags')

class RutaSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Ruta
		fields = ('url', 'nombre', 'descripcion', 'ciudad')

class CircuitoSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Circuito
		fields = ('url', 'nombre', 'descripcion', 'ruta', 'lugares')

class CoordenadaSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Coordenada
		fields = ('url', 'location', 'objects', 'empresa')

class RankingSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Ranking
		fields = ('url', 'lugar', 'usuario', 'valor')

class RankingEmpresaSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = RankingEmpresa
		fields = ('url', 'empresa', 'usuario', 'valor')

class RolSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Rol
		fields = ('url', 'nombre', 'descripcion')

class PermisoSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Permiso
		fields = ('url', 'lugar', 'usuario', 'rol')

class GaleriaSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Galeria
		fields = ('url', 'nombre', 'alt', 'path')






