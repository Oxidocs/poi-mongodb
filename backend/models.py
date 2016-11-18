# -*- coding: utf-8 -*- 
from django.db import models
from django.contrib.auth.models import User
from django_mongodb_engine.contrib import MongoDBManager
from djangotoolbox.fields import EmbeddedModelField, ListField

class Sexo(models.Model):
	valor_arabe = models.CharField(max_length=50, blank=True)
	valor_chino = models.CharField(max_length=50, blank=True)
	valor_espanol = models.CharField(max_length=50, blank=True)
	valor_frances = models.CharField(max_length=50, blank=True)
	valor_ingles = models.CharField(max_length=50, blank=True)
	valor_ruso = models.CharField(max_length=50, blank=True)
	valor_portuges = models.CharField(max_length=50, blank=True)
	def __unicode__(self):
		return u'%s' % self.valor_espanol
	class Meta:
		verbose_name_plural = "Sexos"

class Perfiles(models.Model):
	fecha_de_nac = models.DateField(auto_now=False,auto_now_add=False, blank=True)
	usuario = models.ForeignKey(User)
	sexo = EmbeddedModelField(Sexo)
	image = models.ImageField(upload_to='profiles/')

	def __unicode__(self):
		return u'%s' % self.usuario
	class Meta:
		verbose_name_plural = "Perfiles"

class Categorias(models.Model):
	nombre_arabe = models.CharField(max_length=255, blank=True)
	nombre_chino = models.CharField(max_length=255, blank=True)
	nombre_espanol = models.CharField(max_length=255, blank=True)
	nombre_frances = models.CharField(max_length=255, blank=True)
	nombre_ingles = models.CharField(max_length=255, blank=True)
	nombre_ruso = models.CharField(max_length=255, blank=True)
	nombre_portuges = models.CharField(max_length=255, blank=True)

	descripcion_arabe = models.CharField(max_length=500, blank=True)
	descripcion_chino = models.CharField(max_length=500, blank=True)
	descripcion_espanol = models.CharField(max_length=500, blank=True)
	descripcion_frances = models.CharField(max_length=500, blank=True)
	descripcion_ingles = models.CharField(max_length=500, blank=True)
	descripcion_ruso = models.CharField(max_length=500, blank=True)
	descripcion_portuges = models.CharField(max_length=500, blank=True)

	def __unicode__(self):
		return u'%s' % self.nombre_espanol
	class Meta:
		verbose_name_plural = "Categorías"

class Subcategorias(models.Model):
	nombre_arabe = models.CharField(max_length=255, blank=True)
	nombre_chino = models.CharField(max_length=255, blank=True)
	nombre_espanol = models.CharField(max_length=255, blank=True)
	nombre_frances = models.CharField(max_length=255, blank=True)
	nombre_ingles = models.CharField(max_length=255, blank=True)
	nombre_ruso = models.CharField(max_length=255, blank=True)
	nombre_portuges = models.CharField(max_length=255, blank=True)

	descripcion_arabe = models.CharField(max_length=500, blank=True)
	descripcion_chino = models.CharField(max_length=500, blank=True)
	descripcion_espanol = models.CharField(max_length=500, blank=True)
	descripcion_frances = models.CharField(max_length=500, blank=True)
	descripcion_ingles = models.CharField(max_length=500, blank=True)
	descripcion_ruso = models.CharField(max_length=500, blank=True)
	descripcion_portuges = models.CharField(max_length=500, blank=True)

	categoria = models.ForeignKey(Categorias)

	def __unicode__(self):
		return u'%s' % self.nombre_espanol
	class Meta:
		verbose_name_plural = "Sub Categorías"

class Pais(models.Model):
	nombre_arabe = models.CharField(max_length=255, blank=True)
	nombre_chino = models.CharField(max_length=255, blank=True)
	nombre_espanol = models.CharField(max_length=255, blank=True)
	nombre_frances = models.CharField(max_length=255, blank=True)
	nombre_ingles = models.CharField(max_length=255, blank=True)
	nombre_ruso = models.CharField(max_length=255, blank=True)
	nombre_portuges = models.CharField(max_length=255, blank=True)

	def __unicode__(self):
		return str(self.nombre_espanol)
	class Meta:
		verbose_name_plural = "Países"

class Ciudades(models.Model):
	nombre_arabe = models.CharField(max_length=255, blank=True)
	nombre_chino = models.CharField(max_length=255, blank=True)
	nombre_espanol = models.CharField(max_length=255, blank=True)
	nombre_frances = models.CharField(max_length=255, blank=True)
	nombre_ingles = models.CharField(max_length=255, blank=True)
	nombre_ruso = models.CharField(max_length=255, blank=True)
	nombre_portuges = models.CharField(max_length=255, blank=True)

	pais = models.ForeignKey(Pais)

	def __unicode__(self):
		return u'%s' % self.nombre_espanol
	class Meta:
		verbose_name_plural = "Ciudades"

class Lugares(models.Model):
	categoria = models.ForeignKey(Categorias, null=True, blank=True)
	ciudad = EmbeddedModelField(Ciudades, null=True, blank=True)
	nombre_arabe = models.CharField(max_length=255, blank=True)
	nombre_chino = models.CharField(max_length=255, blank=True)
	nombre_espanol = models.CharField(max_length=255, blank=True)
	nombre_frances = models.CharField(max_length=255, blank=True)
	nombre_ingles = models.CharField(max_length=255, blank=True)
	nombre_ruso = models.CharField(max_length=255, blank=True)
	nombre_portuges = models.CharField(max_length=255, blank=True)

	direccion = models.CharField(max_length=255, blank=True)
	icono = models.CharField(max_length=255, blank=True)
	portada = models.CharField(max_length=255, blank=True)

	descripcion_arabe = models.CharField(max_length=500, blank=True)
	descripcion_chino = models.CharField(max_length=500, blank=True)
	descripcion_espanol = models.CharField(max_length=500, blank=True)
	descripcion_frances = models.CharField(max_length=500, blank=True)
	descripcion_ingles = models.CharField(max_length=500, blank=True)
	descripcion_ruso = models.CharField(max_length=500, blank=True)
	descripcion_portuges = models.CharField(max_length=500, blank=True)

	sitio_web = models.CharField(max_length=500, blank=True)
	fecha_de_creacion = models.DateTimeField(auto_now_add=True, blank=True)
	def __unicode__(self):
		return u'%s' % self.nombre_espanol
	class Meta:
		verbose_name_plural = "Lugares"

class Empresas(models.Model):
	categoria = models.ForeignKey(Categorias, blank=True)
	ciudad = EmbeddedModelField(Ciudades, blank=True)
	nombre_arabe = models.CharField(max_length=255, blank=True)
	nombre_chino = models.CharField(max_length=255, blank=True)
	nombre_espanol = models.CharField(max_length=255, blank=True)
	nombre_frances = models.CharField(max_length=255, blank=True)
	nombre_ingles = models.CharField(max_length=255, blank=True)
	nombre_ruso = models.CharField(max_length=255, blank=True)
	nombre_portuges = models.CharField(max_length=255, blank=True)

	direccion = models.CharField(max_length=255, blank=True)
	icono = models.CharField(max_length=255, blank=True)
	portada = models.CharField(max_length=255, blank=True)

	descripcion_arabe = models.CharField(max_length=500, blank=True)
	descripcion_chino = models.CharField(max_length=500, blank=True)
	descripcion_espanol = models.CharField(max_length=500, blank=True)
	descripcion_frances = models.CharField(max_length=500, blank=True)
	descripcion_ingles = models.CharField(max_length=500, blank=True)
	descripcion_ruso = models.CharField(max_length=500, blank=True)
	descripcion_portuges = models.CharField(max_length=500, blank=True)
	
	sitio_web = models.CharField(max_length=500, blank=True)
	fecha_de_creacion = models.DateTimeField(auto_now_add=True, blank=True)
	def __unicode__(self):
		return u'%s' % self.nombre_espanol
	class Meta:
		verbose_name_plural = "Empresas"

class Rutas(models.Model):
	nombre_arabe = models.CharField(max_length=255, blank=True)
	nombre_chino = models.CharField(max_length=255, blank=True)
	nombre_espanol = models.CharField(max_length=255, blank=True)
	nombre_frances = models.CharField(max_length=255, blank=True)
	nombre_ingles = models.CharField(max_length=255, blank=True)
	nombre_ruso = models.CharField(max_length=255, blank=True)
	nombre_portuges = models.CharField(max_length=255, blank=True)

	descripcion_arabe = models.CharField(max_length=500, blank=True)
	descripcion_chino = models.CharField(max_length=500, blank=True)
	descripcion_espanol = models.CharField(max_length=500, blank=True)
	descripcion_frances = models.CharField(max_length=500, blank=True)
	descripcion_ingles = models.CharField(max_length=500, blank=True)
	descripcion_ruso = models.CharField(max_length=500, blank=True)
	descripcion_portuges = models.CharField(max_length=500, blank=True)

	ciudad = models.CharField(max_length=255)
	def __unicode__(self):
		return u'%s' % self.nombre_espanol
	class Meta:
		verbose_name_plural = "Rutas"

class Circuitos(models.Model):
	nombre_arabe = models.CharField(max_length=255, blank=True)
	nombre_chino = models.CharField(max_length=255, blank=True)
	nombre_espanol = models.CharField(max_length=255, blank=True)
	nombre_frances = models.CharField(max_length=255, blank=True)
	nombre_ingles = models.CharField(max_length=255, blank=True)
	nombre_ruso = models.CharField(max_length=255, blank=True)
	nombre_portuges = models.CharField(max_length=255, blank=True)

	descripcion_arabe = models.CharField(max_length=500, blank=True)
	descripcion_chino = models.CharField(max_length=500, blank=True)
	descripcion_espanol = models.CharField(max_length=500, blank=True)
	descripcion_frances = models.CharField(max_length=500, blank=True)
	descripcion_ingles = models.CharField(max_length=500, blank=True)
	descripcion_ruso = models.CharField(max_length=500, blank=True)
	descripcion_portuges = models.CharField(max_length=500, blank=True)

	ruta = models.ForeignKey(Rutas)
	lugares = models.ManyToManyField(Lugares)
	def __unicode__(self):
		return u'%s' % self.nombre_espanol
	class Meta:
		verbose_name_plural = "Circuitos"

class Point(models.Model):
	latitude = models.FloatField()
	longtitude = models.FloatField()
	def __unicode__(self):
		return u'%s , %s' % (self.latitude, self.longtitude)
	class Meta:
		verbose_name_plural = "Puntos"

class Coordenadas(models.Model):
	location = EmbeddedModelField(Point)
	objects = MongoDBManager()
	lugar = models.ForeignKey(Lugares,null=True , blank=True)
	empresa = models.ForeignKey(Empresas,null=True , blank=True)
	def __unicode__(self):
		return u'%s' % self.lugar
	class Meta:
		verbose_name_plural = "Coordenadas"

class Ranking(models.Model):
	lugar = models.ForeignKey(Lugares)
	usuario = models.ForeignKey(User)
	valor = models.IntegerField(default=0)
	def __unicode__(self):
		return u'%s' % self.lugar
	class Meta:
		verbose_name_plural = "Ranking"

class RankingEmpresa(models.Model):
	empresa = models.ForeignKey(Empresas)
	usuario = models.ForeignKey(User)
	valor = models.IntegerField(default=0)
	def __unicode__(self):
		return u'%s' % self.empresa
	class Meta:
		verbose_name_plural = "Ranking"

class Roles(models.Model):
	nombre_arabe = models.CharField(max_length=255, blank=True)
	nombre_chino = models.CharField(max_length=255, blank=True)
	nombre_espanol = models.CharField(max_length=255, blank=True)
	nombre_frances = models.CharField(max_length=255, blank=True)
	nombre_ingles = models.CharField(max_length=255, blank=True)
	nombre_ruso = models.CharField(max_length=255, blank=True)
	nombre_portuges = models.CharField(max_length=255, blank=True)

	descripcion_arabe = models.CharField(max_length=500, blank=True)
	descripcion_chino = models.CharField(max_length=500, blank=True)
	descripcion_espanol = models.CharField(max_length=500, blank=True)
	descripcion_frances = models.CharField(max_length=500, blank=True)
	descripcion_ingles = models.CharField(max_length=500, blank=True)
	descripcion_ruso = models.CharField(max_length=500, blank=True)
	descripcion_portuges = models.CharField(max_length=500, blank=True)
	def __unicode__(self):
		return u'%s' % self.nombre_espanol
	class Meta:
		verbose_name_plural = "Roles"

class Permisos(models.Model):
	lugar = models.ForeignKey(Lugares)
	usuario = models.ForeignKey(User)
	rol = models.ForeignKey(Roles)
	def __unicode__(self):
		return u'%s' % self.usuario
	class Meta:
		verbose_name_plural = "Permisos"

class Galerias(models.Model):
	nombre_arabe = models.CharField(max_length=255, blank=True)
	nombre_chino = models.CharField(max_length=255, blank=True)
	nombre_espanol = models.CharField(max_length=255, blank=True)
	nombre_frances = models.CharField(max_length=255, blank=True)
	nombre_ingles = models.CharField(max_length=255, blank=True)
	nombre_ruso = models.CharField(max_length=255, blank=True)
	nombre_portuges = models.CharField(max_length=255, blank=True)

	alt = models.CharField(max_length=255)
	path = models.CharField(max_length=255)
	def __unicode__(self):
		return u'%s' % self.nombre_espanol
	class Meta:
		verbose_name_plural = "Galerías"

class RedesSociales(models.Model):
	lugar = models.ForeignKey(Lugares)
	link = models.CharField(max_length=255)
	def __unicode__(self):
		return u'%s' % self.lugar
	class Meta:
		verbose_name_plural = "Redes Sociales"

class Tag(models.Model):
	valor = models.CharField(max_length=255)
	lugar = models.ForeignKey(Lugares)
	def __unicode__(self):
		return u'%s' % self.lugar

class Email(models.Model):
	valor = models.EmailField(max_length=100, unique= True)
	lugar = models.ForeignKey(Lugares, blank=True)
	perfil = models.ForeignKey(Perfiles, blank=True)
	def __unicode__(self):
		return u'%s' % self.valor

class Telefonos(models.Model):
	valor = models.IntegerField()
	lugar = models.ForeignKey(Lugares, blank=True)
	perfil = models.ForeignKey(Perfiles, blank=True)
	def __unicode__(self):
		return u'%s' % self.valor
	class Meta:
		verbose_name_plural = "Teléfonos"
