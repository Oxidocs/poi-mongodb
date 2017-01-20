from django.shortcuts import render#, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from backend.models import Perfil, Lugar, Coordenada, Point, Sexo, Nombre
from backend.perfil import getPerfil, validarUsuario
import datetime, locale

from django.contrib import messages

@login_required(login_url='/plataforma/login/')
def Index(request):
	response = {
		'perfil': getPerfil(request)
	}
	return validarUsuario(request, 'plataforma/index.html', response, "render")

@login_required(login_url='/plataforma/login/')
def Destinos(request):
	response = {
		'perfil': getPerfil(request)
	}
	return validarUsuario(request, 'plataforma/destinos.html',response, "render")

@login_required(login_url='/plataforma/login/')
def Servicios(request):
	response = {
		'perfil': getPerfil(request)
	}
	return validarUsuario(request, 'plataforma/servicios.html', response, "render")

@login_required(login_url='/plataforma/login/')
def Productos(request):
	response = {
		'perfil': getPerfil(request)
	}
	return validarUsuario(request, 'plataforma/productos.html', response, "render")

@login_required(login_url='/plataforma/login/')
def Circuitos(request):
	response = {
		'perfil': getPerfil(request)
	}
	return validarUsuario(request, 'plataforma/circuitos.html', response, "render")

@login_required(login_url='/plataforma/login/')
def Rutas(request):
	response = {
		'perfil': getPerfil(request)
	}
	return validarUsuario(request, 'plataforma/rutas.html', response, "render")

@login_required(login_url='/plataforma/login/')
def Estadisticas(request):
	response = {
		'perfil': getPerfil(request)
	}
	return validarUsuario(request, 'plataforma/estadisticas.html', response, "render")

@login_required(login_url='/plataforma/login/')
def Informes(request):
	response = {
		'perfil': getPerfil(request)
	}
	return validarUsuario(request, 'plataforma/informes.html', response, "render")

@login_required(login_url='/plataforma/login/')
def Calendarios(request):
	response = {
		'perfil': getPerfil(request)
	}
	return validarUsuario(request, 'plataforma/calendarios.html', response, "render")


@login_required(login_url='/plataforma/login/')
def editarPerfil(request):

	locale.setlocale(locale.LC_ALL, "")

	if request.method=='POST':

		if 'img_perfil' in request.FILES:
			img = request.FILES['img_perfil']
		else:
			img = ""

		data = request.POST

		username=data.get('username')
		nombres=data.get('nombres')
		apellidos=data.get('apellidos')
		email=data.get('email')
		sexo=data.get('sexo')
		fecha_de_nac=data.get('fecha_de_nac')

		if fecha_de_nac != "":				
			fecha_de_nac = datetime.datetime.strptime(fecha_de_nac, '%d %B %Y').strftime("%Y-%m-%d")

		sexo_doument = Sexo(
			valor_arabe = "",
			valor_chino = "",
			valor_espanol = sexo,
			valor_frances = "",
			valor_ingles = "",
			valor_ruso = "",
			valor_portuges = ""
		)

		######### Obteniendo Usuario #############

		usuario = User.objects.filter(pk=request.user.id).first()

		if username!='':
			usuario.username = username
		if nombres!='':
			usuario.first_name = nombres 
		if apellidos!='':
			usuario.last_name = apellidos
		if email!='':
			usuario.email = email

		usuario.save() #actualizar usuario

		######### Obteniendo Perfil de Usuario #############

		perfil = Perfil.objects.filter(usuario__pk=request.user.id).first()

		if perfil is None:
			Perfil(
				usuario = request.user,
				sexo = sexo_doument,
				fecha_de_nac = fecha_de_nac,
				image = img
			).save() #crear perfil
		else:
			if sexo is not None:
				perfil.sexo = sexo_doument

			if fecha_de_nac != "":
				perfil.fecha_de_nac = fecha_de_nac
			
			if img != "":
				perfil.image = img

			perfil.save() #actualizar perfil
		

		response ={
			'data': [username, nombres, apellidos, email, sexo, fecha_de_nac]
		}
		return validarUsuario(request, '', response, "json")
	else:
		response = {
			'perfil': getPerfil(request)
		}
		return validarUsuario(request, 'plataforma/editar_perfil.html', response, "render")

def saveLugar(request):

	latitude = request.POST.get('lat')
	longitude =request.POST.get('long')

	lugar = Lugar.objects.all().count()
	lugar = lugar + 1
	nombre = "Lugar %s" % lugar

	nombre = Nombre(
			nombre_arabe = "",
			nombre_chino = "",
			nombre_espanol = nombre,
			nombre_frances = "",
			nombre_ingles = "",
			nombre_ruso = "",
			nombre_portuges = ""
	 	)

	point = Point(
		latitude = latitude,
		longtitude = longitude
	)
		

	lugar = Lugar(
		nombre = nombre,
		location = point
	).save()

	lugar = Lugar.objects.latest('id').id

	return validarUsuario(request, '', lugar, "json")

def getLugar(request):

	lugar_id = request.POST.get('id')

	lugar = Lugar.objects.get(pk=lugar_id);
	fecha_de_creacion = ""
	portada = "";
	icono = "";

	if lugar.icono is not None and lugar.icono != "":
		icono = lugar.icono	
	if lugar.icono is not None and lugar.icono != "":
		portada = lugar.portada

	if lugar.fecha_de_creacion != "":
		print lugar.fecha_de_creacion
		fecha_de_creacion = lugar.fecha_de_creacion.strftime("%Y-%m-%d")

	context = {
		'id' : lugar.id,
		'nombre': lugar.nombre.nombre_espanol,
		'descripcion': lugar.descripcion,
		'categoria': lugar.categoria,
		'ciudad': lugar.ciudad,
		'latitude': lugar.location.latitude,
		'longtitude': lugar.location.longtitude,
		'direccion': lugar.direccion,
		'icono': icono,
		'portada': portada,
		'sitio_web': lugar.sitio_web,
		'redes_sociales': lugar.redes_sociales,
		'fecha_de_creacion': fecha_de_creacion,
		'tags': lugar.tags
	}
	

	return validarUsuario(request,'',context, "json")


