from backend.models import Perfil, Sexo


def getPerfil(request):
	imagen = '/profiles/default/img.jpg'

	sexo = Sexo.objects.all()
	perfil = Perfil.objects.filter(usuario__pk=request.user.id).first()
	print perfil

	if perfil is not None:
		if perfil.image is not None and perfil.image != "":
			imagen = perfil.image.name

	response = {
		'sexos': sexo,
		'imagen_perfil': '/media%s' %imagen
	}

	return response