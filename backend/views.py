from django.shortcuts import render#, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from backend.models import Perfil, Lugar, Coordenada, Point, Sexo
from .forms import ProfileForm, UserForm
import json

from django.contrib import messages

@login_required(login_url='/plataforma/login/')
def Index(request):
	return render(request, 'plataforma/index.html')

@login_required(login_url='/plataforma/login/')
def editarPerfil(request):

	sexo = Sexo.objects.all()

	if request.method == "POST":
		form = ProfileForm(request.POST, request.FILES)
		user = UserForm()

		if form.is_valid():
			perfil = form.save(commit=False)
			perfil.usuario = request.user
			perfil.sexo = Sexo(valor_espanol=request.POST['sexo'])
			perfil.save()
			render(request, 'plataforma/editar_perfil.html')

	else:
		form = ProfileForm()
		user = UserForm()

	response = {
		'perfiles': form,
		'users': user,
		'sexos': sexo,
	}

	return render(request, 'plataforma/editar_perfil.html', response)

@login_required(login_url='/plataforma/login/')
def Destinos(request):
	return render(request, 'plataforma/destinos.html')

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

def getPerfil(request):

	id_user = request.POST.get('id')
	perfil = Perfil.objects.filter(usuario__pk=id_user).first()
	imagen = '/profiles/default/img.jpg'

	if perfil is not None:
		if perfil.image is not None:
			if perfil.image != "":
				imagen = perfil.image.name
			
	context = {
		'imagen': imagen,
	}

	return HttpResponse(json.dumps(context), content_type="application/json")

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
