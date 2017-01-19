# -*- coding: utf-8 -*- 
from django.db import models
from django.contrib.auth.models import User
from django_mongodb_engine.contrib import MongoDBManager
from djangotoolbox.fields import EmbeddedModelField, ListField
from .listfield import StringListField

class Nombre(models.Model):
	nombre_arabe = models.CharField(max_length=255, blank=True)
	nombre_chino = models.CharField(max_length=255, blank=True)
	nombre_espanol = models.CharField(max_length=255, blank=True)
	nombre_frances = models.CharField(max_length=255, blank=True)
	nombre_ingles = models.CharField(max_length=255, blank=True)
	nombre_ruso = models.CharField(max_length=255, blank=True)
	nombre_portuges = models.CharField(max_length=255, blank=True)
	def __unicode__(self):
		return u'{nombre_arabe: %s,nombre_chino: %s,nombre_espanol: %s,nombre_frances: %s,nombre_ingles: %s,nombre_ruso: %s,nombre_portuges: %s}' % (self.nombre_arabe, self.nombre_chino, self.nombre_espanol, self.nombre_frances, self.nombre_ingles, self.nombre_ruso, self.nombre_portuges)
	class Meta:
		verbose_name_plural = "Nombres"

class Descripcion(models.Model):
	descripcion_arabe = models.CharField(max_length=500, blank=True)
	descripcion_chino = models.CharField(max_length=500, blank=True)
	descripcion_espanol = models.CharField(max_length=500, blank=True)
	descripcion_frances = models.CharField(max_length=500, blank=True)
	descripcion_ingles = models.CharField(max_length=500, blank=True)
	descripcion_ruso = models.CharField(max_length=500, blank=True)
	descripcion_portuges = models.CharField(max_length=500, blank=True)
	def __unicode__(self):
		return u'{descripcion_arabe: %s, descripcion_chino: %s, descripcion_espanol: %s, descripcion_frances: %s, descripcion_ingles: %s, descripcion_ruso: %s, descripcion_portuges: %s}' % (descripcion_arabe, descripcion_chino, descripcion_espanol, descripcion_frances, descripcion_ingles, descripcion_ruso, descripcion_portuges)
	class Meta:
		verbose_name_plural = "Descripciones"

class Tag(models.Model):
	valor = models.CharField(max_length=255)
	def __unicode__(self):
		return u'%s' % self.valor
	class Meta:
		verbose_name_plural = "Tags"

class RedSocial(models.Model):
	link = models.CharField(max_length=255)
	def __unicode__(self):
		return u'%s' % self.link
	class Meta:
		verbose_name_plural = "Redes Sociales"

class Sexo(models.Model):
	valor_arabe = models.CharField(max_length=50, blank=True)
	valor_chino = models.CharField(max_length=50, blank=True)
	valor_espanol = models.CharField(max_length=50, blank=True)
	valor_frances = models.CharField(max_length=50, blank=True)
	valor_ingles = models.CharField(max_length=50, blank=True)
	valor_ruso = models.CharField(max_length=50, blank=True)
	valor_portuges = models.CharField(max_length=50, blank=True)
	def __unicode__(self):
		return u'{valor_arabe: %s,valor_chino: %s,valor_espanol: %s,valor_frances: %s,valor_ingles: %s,valor_ruso: %s,valor_portuges: %s}' % (self.valor_arabe, self.valor_chino, self.valor_espanol, self.valor_frances, self.valor_ingles, self.valor_ruso, self.valor_portuges)
	class Meta:
		verbose_name_plural = "Sexos"

class EmailField(ListField):
	def formfield(self, **kwargs):
		return models.Field.formfield(self, StringListField, **kwargs)

class Perfil(models.Model):
	usuario = models.ForeignKey(User)
	sexo = EmbeddedModelField(Sexo, blank=True, null=True)
	emails = EmailField()
	telefonos = ListField(blank=True, null=True)
	fecha_de_nac = models.DateField(auto_now=False,auto_now_add=False, blank=True, null=True)
	image = models.ImageField(upload_to='profiles/', blank=True, null=True)
	def __unicode__(self):
		return u'%s' % self.usuario
	class Meta:
		verbose_name_plural = "Perfiles"

class Categoria(models.Model):
	nombre = EmbeddedModelField(Nombre)
	descripcion = EmbeddedModelField(Descripcion)

	def __unicode__(self):
		return u'%s' % self.nombre
	class Meta:
		verbose_name_plural = "Categorías"

class Subcategoria(models.Model):
	nombre = EmbeddedModelField(Nombre)
	descripcion = EmbeddedModelField(Descripcion)
	categoria = models.ForeignKey(Categoria)

	def __unicode__(self):
		return u'%s' % self.nombre
	class Meta:
		verbose_name_plural = "Sub Categorías"

class Pais(models.Model):
	nombre = EmbeddedModelField(Nombre)

	def __unicode__(self):
		return str(self.nombre)
	class Meta:
		verbose_name_plural = "Países"

class Ciudad(models.Model):
	nombre = EmbeddedModelField(Nombre)
	pais = models.ForeignKey(Pais)

	def __unicode__(self):
		return u'%s' % self.nombre
	class Meta:
		verbose_name_plural = "Ciudades"

class Point(models.Model):
	latitude = models.FloatField()
	longtitude = models.FloatField()
	def __unicode__(self):
		return u'{latitude: %s , longitude: %s}' % (self.latitude, self.longtitude)
	class Meta:
		verbose_name_plural = "Puntos"

class Lugar(models.Model):
	nombre = EmbeddedModelField(Nombre)
	descripcion = EmbeddedModelField(Descripcion, null=True, blank=True)
	categoria = models.ForeignKey(Categoria, null=True, blank=True)
	ciudad = EmbeddedModelField(Ciudad, null=True, blank=True)
	location = EmbeddedModelField(Point, blank=True, null=True)
	objects = MongoDBManager()
	direccion = models.CharField(max_length=255, blank=True)
	icono = models.ImageField(upload_to='iconos/')
	portada = models.ImageField(upload_to='portadas/')
	sitio_web = models.CharField(max_length=500, blank=True)
	redes_sociales = ListField(EmbeddedModelField(RedSocial))
	fecha_de_creacion = models.DateTimeField(auto_now_add=True, blank=True)
	tags = EmbeddedModelField(Tag, null=True, blank=True)
	def __unicode__(self):
		return u'%s' % self.nombre
	class Meta:
		verbose_name_plural = "Lugares"

class Empresa(models.Model):
	nombre = EmbeddedModelField(Nombre)
	email = EmailField()
	telefonos = ListField(blank=True, null=True)
	descripcion = EmbeddedModelField(Descripcion)
	categoria = models.ForeignKey(Categoria, blank=True)
	ciudad = EmbeddedModelField(Ciudad, blank=True)
	direccion = models.CharField(max_length=255, blank=True)
	icono = models.ImageField(upload_to='iconos/')
	portada = models.ImageField(upload_to='portadas/')
	redes_sociales = ListField(EmbeddedModelField(RedSocial))
	sitio_web = models.CharField(max_length=500, blank=True)
	fecha_de_creacion = models.DateTimeField(auto_now_add=True, blank=True)
	tags = EmbeddedModelField(Tag)
	def __unicode__(self):
		return u'%s' % self.nombre
	class Meta:
		verbose_name_plural = "Empresas"

class Ruta(models.Model):
	nombre = EmbeddedModelField(Nombre)
	descripcion = EmbeddedModelField(Descripcion)
	ciudad = models.CharField(max_length=255)
	def __unicode__(self):
		return u'%s' % self.nombre
	class Meta:
		verbose_name_plural = "Rutas"

class Circuito(models.Model):
	nombre = EmbeddedModelField(Nombre)
	descripcion = EmbeddedModelField(Descripcion)
	ruta = models.ForeignKey(Ruta)
	lugares = models.ManyToManyField(Lugar)
	def __unicode__(self):
		return u'%s' % self.nombre
	class Meta:
		verbose_name_plural = "Circuitos"

class Coordenada(models.Model):
	location = EmbeddedModelField(Point)
	objects = MongoDBManager()
	empresa = models.ForeignKey(Empresa,null=True , blank=True)
	def __unicode__(self):
		return u'%s' % self.empresa
	class Meta:
		verbose_name_plural = "Coordenadas"

class Ranking(models.Model):
	lugar = models.ForeignKey(Lugar)
	usuario = models.ForeignKey(User)
	valor = models.IntegerField(default=0)
	def __unicode__(self):
		return u'%s' % self.lugar
	class Meta:
		verbose_name_plural = "Ranking"

class RankingEmpresa(models.Model):
	empresa = models.ForeignKey(Empresa)
	usuario = models.ForeignKey(User)
	valor = models.IntegerField(default=0)
	def __unicode__(self):
		return u'%s' % self.empresa
	class Meta:
		verbose_name_plural = "Ranking"

class Rol(models.Model):
	nombre = EmbeddedModelField(Nombre)
	descripcion = EmbeddedModelField(Descripcion)
	def __unicode__(self):
		return u'%s' % self.nombre
	class Meta:
		verbose_name_plural = "Roles"

class Permiso(models.Model):
	lugar = models.ForeignKey(Lugar)
	usuario = models.ForeignKey(User)
	rol = models.ForeignKey(Rol)
	def __unicode__(self):
		return u'%s' % self.usuario
	class Meta:
		verbose_name_plural = "Permisos"

class Galeria(models.Model):
	nombre = EmbeddedModelField(Nombre)
	alt = models.CharField(max_length=255)
	path = models.CharField(max_length=255)
	def __unicode__(self):
		return u'%s' % self.nombre
	class Meta:
		verbose_name_plural = "Galerías"
