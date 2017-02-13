from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User
from backend.models import Perfil, Sexo
from django.shortcuts import render
import json, datetime, locale


def getPerfil(request):
	imagen = '/profiles/default/img.jpg'

	sexo = Sexo.objects.all()
	perfil = Perfil.objects.filter(usuario__pk=request.user.id).first()

	if perfil is not None:
		if perfil.image is not None and perfil.image != "":
			imagen = '/%s' %perfil.image.name
		
		fecha_de_nac = perfil.fecha_de_nac
		print fecha_de_nac

	response = {
		'full': perfil,
		'sexos': sexo,
		'imagen_perfil': '/media%s' %imagen
	}

	return response

def editPerfil(request):
	locale.setlocale(locale.LC_ALL, "")

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

	return response

def validarUsuario(request, template, response, type):
	if request.user.is_staff:
		if type == "render":
			return render(request, template, response)
		elif type == "json":
			return HttpResponse(json.dumps(response), content_type="application/json")
	else:
		return HttpResponseRedirect('/plataforma/login/')