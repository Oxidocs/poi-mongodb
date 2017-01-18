from backend.models import Perfil, Sexo
import datetime


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