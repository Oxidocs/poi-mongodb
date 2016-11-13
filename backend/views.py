from django.shortcuts import render#, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from backend.models import Perfiles
import json

from django.contrib import messages

@login_required(login_url='/plataforma/login/')
def Index(request):
	return render(request, 'plataforma/index.html')

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
	perfil = Perfiles.objects.filter(usuario__pk=id_user).first()
	if perfil.image is not None:
		imagen = perfil.image.name
	else:
		imagen = '/media/prfiles/images/img.jpg'
		
	context = {
		'imagen': imagen,
	}

	return HttpResponse(json.dumps(context), content_type="application/json")
