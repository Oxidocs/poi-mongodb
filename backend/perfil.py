from django.http import HttpResponse, HttpResponseRedirect
from backend.models import Perfil, Sexo
from django.shortcuts import render
import json


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

def validarUsuario(request, template, response, type):
	if request.user.is_staff:
		if type == "render":
			return render(request, template, response)
		elif type == "json":
			return HttpResponse(json.dumps(response), content_type="application/json")
	else:
		return HttpResponseRedirect('/plataforma/login/')