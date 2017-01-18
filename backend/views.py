from django.shortcuts import render#, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from backend.models import Perfil, Lugar, Coordenada, Point, Sexo
from backend.perfil import getPerfil
import json

from django.contrib import messages

@login_required(login_url='/plataforma/login/')
def Index(request):
	response = {
		'perfil': getPerfil(request)
	}
	return render(request, 'plataforma/index.html', response)

@login_required(login_url='/plataforma/login/')
def Destinos(request):
	response = {
		'perfil': getPerfil(request)
	}
	return render(request, 'plataforma/destinos.html',response)

@login_required(login_url='/plataforma/login/')
def Servicios(request):
	return render(request, 'plataforma/servicios.html')

@login_required(login_url='/plataforma/login/')
def Productos(request):
	return render(request, 'plataforma/productos.html')

@login_required(login_url='/plataforma/login/')
def Circuitos(request):
	return render(request, 'plataforma/circuitos.html')

@login_required(login_url='/plataforma/login/')
def Rutas(request):
	return render(request, 'plataforma/rutas.html')

@login_required(login_url='/plataforma/login/')
def Estadisticas(request):
	return render(request, 'plataforma/estadisticas.html')

@login_required(login_url='/plataforma/login/')
def Informes(request):
	return render(request, 'plataforma/informes.html')

@login_required(login_url='/plataforma/login/')
def Calendarios(request):
	return render(request, 'plataforma/calendarios.html')


@login_required(login_url='/plataforma/login/')
def editarPerfil(request):
	
		#if request.method == "POST":
		# if form.is_valid():
		# 	perfil = form.save(commit=False)
		# 	perfil.usuario = request.user
		# 	perfil.sexo = Sexo(valor_espanol=request.POST['sexo'])
		# 	perfil.save()
		# 	render(request, 'plataforma/editar_perfil.html')

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

		sexo_doument = Sexo(
			valor_arabe = "",
			valor_chino = "",
			valor_espanol = sexo,
			valor_frances = "",
			valor_ingles = "",
			valor_ruso = "",
			valor_portuges = ""
		)

		perfil = Perfil.objects.filter(usuario__pk=request.user.id).first()
		if perfil is None:
			
			Perfil(
				usuario = request.user,
				sexo = sexo_doument,
				#fecha_de_nac = fecha_de_nac,
				image = img
			).save()
		else:
			if sexo is not None:				
				perfil.sexo = sexo_doument
			
			#perfil.fecha_de_nac = fecha_de_nac,
			
			if img!="":
				perfil.image = img

			perfil.save()
		

		response ={
			'data': [username, nombres, apellidos, email, sexo, fecha_de_nac]
		}
		return HttpResponse(json.dumps(response), content_type="application/json")
	else:
		response = {
			'perfil': getPerfil(request)			
		}
		return render(request, 'plataforma/editar_perfil.html', response)

def saveLugar(request):

	latitude = request.POST.get('lat')
	longitude =request.POST.get('long')

	lugar = Lugar.objects.all().count()
	lugar = lugar + 1
	nombre = "Lugar %s" % lugar

	Lugar(nombre_espanol = nombre).save()

	lugar = Lugar.objects.latest('id').id

	Coordenada(lugar_id=lugar, location=Point(latitude=latitude,longtitude=longitude)).save()

	return HttpResponse(json.dumps(lugar), content_type="application/json")

def getLugar(request):

	lugar_id = request.POST.get('id')

	lugar = Lugar.objects.get(pk=lugar_id);

	context = {
		'id' : lugar.id,
	}
	

	return HttpResponse(json.dumps(context), content_type="application/json")
