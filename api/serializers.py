from django.contrib.auth.models import User, Group
from rest_framework import serializers
from backend.models import Rutas, Perfiles


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

class RutasSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Rutas
		fields = ('url', 'nombre', 'descripcion', 'ciudad')