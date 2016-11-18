from django.contrib.auth.models import User, Group
from rest_framework import serializers
from backend.models import Rutas, Perfiles, Lugares, Categorias, Subcategorias, Empresas, Circuitos
    

class UserSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = User
		fields = ('url', 'username', 'email')


class GroupSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Group
		fields = ('url', 'name')

class PerfilesSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Perfiles
		fields = ('url', 'fecha_de_nac', 'usuario', 'sexo', 'image')

class CategoriasSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Categorias
		fields = ('url', 'nombre_arabe', 'nombre_chino', 'nombre_espanol', 'nombre_frances', 'nombre_ingles', 'nombre_ruso', 'nombre_portuges', 'descripcion_arabe', 'descripcion_chino', 'descripcion_espanol', 'descripcion_frances', 'descripcion_ingles', 'descripcion_ruso', 'descripcion_portuges')

class SubcategoriasSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Subcategorias
		fields = ('url', 'nombre_arabe', 'nombre_chino', 'nombre_espanol', 'nombre_frances', 'nombre_ingles', 'nombre_ruso', 'nombre_portuges', 'descripcion_arabe', 'descripcion_chino', 'descripcion_espanol', 'descripcion_frances', 'descripcion_ingles', 'descripcion_ruso', 'descripcion_portuges')

class LugaresSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Lugares
		fields = ('url', 'categoria', 'ciudad', 'nombre_arabe', 'nombre_chino', 'nombre_espanol', 'nombre_frances', 'nombre_ingles', 'nombre_ruso', 'nombre_portuges', 'direccion', 'icono', 'portada', 'descripcion_arabe', 'descripcion_chino', 'descripcion_espanol', 'descripcion_frances', 'descripcion_ingles', 'descripcion_ruso', 'descripcion_portuges', 'sitio_web', 'fecha_de_creacion')

class EmpresasSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Empresas
		fields = ('url', 'categoria', 'ciudad', 'nombre_arabe', 'nombre_chino', 'nombre_espanol', 'nombre_frances', 'nombre_ingles', 'nombre_ruso', 'nombre_portuges', 'direccion', 'icono', 'portada', 'descripcion_arabe', 'descripcion_chino', 'descripcion_espanol', 'descripcion_frances', 'descripcion_ingles', 'descripcion_ruso', 'descripcion_portuges', 'sitio_web', 'fecha_de_creacion')

class RutasSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Rutas
		fields = ('url', 'nombre', 'descripcion', 'ciudad')

class CircuitosSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Circuitos
		fields = ('nombre_arabe' ,'nombre_chino' ,'nombre_espanol' ,'nombre_frances' ,'nombre_ingles' ,'nombre_ruso' ,'nombre_portuges' ,	'descripcion_arabe' ,'descripcion_chino' ,'descripcion_espanol' ,'descripcion_frances' ,'descripcion_ingles' ,'descripcion_ruso' ,'descripcion_portuges' ,)


