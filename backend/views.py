from django.shortcuts import render#, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from backend.usuario import getPerfil, editPerfil, validarUsuario
from backend.lugares import guardarLugar, actualizarPosicion, obtenerLugar, obtenerTodosLugares, deletePlace

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

	if request.method=='POST':
		response = editPerfil(request)
		return validarUsuario(request, '', response, "json")
	else:
		response = {
			'perfil': getPerfil(request)
		}
		return validarUsuario(request, 'plataforma/editar_perfil.html', response, "render")

@login_required(login_url='/plataforma/login/')
def saveLugar(request):
	response = guardarLugar(request)
	return validarUsuario(request, '', response, "json")

@login_required(login_url='/plataforma/login/')
def getLugar(request):
	response = obtenerLugar(request)
	return validarUsuario(request,'',response, "json")

@login_required(login_url='/plataforma/login/')
def getTodosLugares(request):
	response = obtenerTodosLugares(request)
	return validarUsuario(request,'',response, "json")

@login_required(login_url='/plataforma/login/')
def editLocation(request):
	response = actualizarPosicion(request)
	return validarUsuario(request,'',response, "json")

@login_required(login_url='/plataforma/login/')
def deleteLugar(request):
	response = deletePlace(request)
	return validarUsuario(request,'',response, "json")
