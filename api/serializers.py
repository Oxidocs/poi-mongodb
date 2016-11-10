from django.contrib.auth.models import User, Group
from rest_framework import serializers
from backend.models import Rutas


class UserSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = User
		fields = ('url', 'username', 'email')


class GroupSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Group
		fields = ('url', 'name')

class RutasSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Rutas
		fields = ('url', 'nombre', 'descripcion', 'ciudad')