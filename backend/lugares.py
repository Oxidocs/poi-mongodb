from backend.models import Lugar, Coordenada, Point, Nombre, Descripcion


def guardarLugar(request):

	latitude = request.POST.get('lat')
	longtitude =request.POST.get('long')
	id_lugar = request.POST.get('id');

	if 'icono' in request.FILES:
		icono = request.FILES['icono']
	else:
		icono = ""

	if 'portada' in request.FILES:
		portada = request.FILES['portada']
	else:
		portada = ""

	if id_lugar is not None:

		latitude = request.POST.get('latitud')
		longtitude =request.POST.get('longitud')
		direccion = request.POST.get('direccion')
		descripcion = request.POST.get('descripcion')
		sitio_web = request.POST.get('sitio_web')

		if request.POST.get('nombre') is None or request.POST.get('nombre')=='':
			lugar = Lugar.objects.all().count()
			lugar = lugar + 1
			nombre = "Lugar %s" % lugar
		else:
			nombre = request.POST.get('nombre')

		if request.POST.get('nombre_ingles') is None or request.POST.get('nombre_ingles')=='':
			nombre_ingles = nombre
		else:
			request.POST.get('nombre_ingles')
			nombre_ingles = request.POST.get('nombre_ingles')		

		if request.POST.get('descripcion_ingles') is None or request.POST.get('descripcion_ingles')=='':
			descripcion_ingles = descripcion
		else:
			descripcion_ingles = request.POST.get('descripcion_ingles')

		nombre_embededd = Nombre(
				nombre_arabe = nombre,
				nombre_chino = nombre,
				nombre_espanol = nombre,
				nombre_frances = nombre,
				nombre_ingles = nombre_ingles,
				nombre_ruso = nombre,
				nombre_portuges = nombre
		 	)

		descripcion_embededd = Descripcion(
				descripcion_arabe = descripcion,
				descripcion_chino = descripcion,
				descripcion_espanol = descripcion,
				descripcion_frances = descripcion,
				descripcion_ingles = descripcion_ingles,
				descripcion_ruso = descripcion,
				descripcion_portuges = descripcion
			)	

		point = Point(
			latitude = latitude,
			longtitude = longtitude
		)

		lugar = Lugar.objects.get(pk=id_lugar)
		lugar.nombre = nombre_embededd
		lugar.descripcion = descripcion_embededd
		lugar.location = point
		lugar.direccion = direccion
		lugar.icono = icono
		lugar.portada = portada
		lugar.sitio_web = sitio_web
		lugar.save()

		context = {
			'id': request.POST.get('id'),
			'nombre_arabe':nombre,
			'nombre_chino':nombre,
			'nombre_espanol':nombre,
			'nombre_frances':nombre,
			'nombre_ingles':nombre_ingles,
			'nombre_ruso':nombre,
			'nombre_portuges':nombre,
			'descripcion_arabe':descripcion,
			'descripcion_chino':descripcion,
			'descripcion_espanol':descripcion,
			'descripcion_frances':descripcion,
			'descripcion_ingles':descripcion_ingles,
			'descripcion_ruso':descripcion,
			'descripcion_portuges':descripcion,
			'latitude': latitude,
			'longtitude': longtitude,
			'sitio_web': sitio_web
		}
		
	else:
		lugar = Lugar.objects.all().count()
		lugar = lugar + 1
		nombre = "Lugar %s" % lugar

		nombre_embededd = Nombre(
				nombre_arabe = nombre,
				nombre_chino = nombre,
				nombre_espanol = nombre,
				nombre_frances = nombre,
				nombre_ingles = nombre,
				nombre_ruso = nombre,
				nombre_portuges = nombre
		 	)

		point = Point(
			latitude = latitude,
			longtitude = longtitude
		)
			

		lugar = Lugar(
			nombre = nombre_embededd,
			location = point
		).save()

		context = {
			'id': Lugar.objects.latest('id').id,
			'nombre_arabe':nombre,
			'nombre_chino':nombre,
			'nombre_espanol':nombre,
			'nombre_frances':nombre,
			'nombre_ingles':nombre,
			'nombre_ruso':nombre,
			'nombre_portuges':nombre,
			'latitude': latitude,
			'longtitude': longtitude
		}

	return context

def actualizarPosicion(request):

	point = Point(
			latitude = request.POST.get('lat'),
			longtitude =  request.POST.get('long')
		)

	lugar = Lugar.objects.get(pk=request.POST.get('id'))
	lugar.location = point
	lugar.save()

	return True

def obtenerLugar(request):
	lugar_id = request.POST.get('id')

	lugar = Lugar.objects.get(pk=lugar_id);
	fecha_de_creacion = ""
	portada = "";
	icono = "";

	if lugar.icono is not None and lugar.icono !="":
		icono = lugar.icono

	if lugar.portada is not None and lugar.portada !="":
		portada = lugar.portada
	
	if lugar.descripcion is not None:
		descripcion = {
			'descripcion_arabe':lugar.descripcion.descripcion_arabe,
			'descripcion_chino':lugar.descripcion.descripcion_chino,
			'descripcion_espanol':lugar.descripcion.descripcion_espanol,
			'descripcion_frances':lugar.descripcion.descripcion_frances,
			'descripcion_ingles':lugar.descripcion.descripcion_ingles,
			'descripcion_ruso':lugar.descripcion.descripcion_ruso,
			'descripcion_portuges':lugar.descripcion.descripcion_portuges
		}
	else:
		descripcion = {
			'descripcion_arabe':'',
			'descripcion_chino':'',
			'descripcion_espanol':'',
			'descripcion_frances':'',
			'descripcion_ingles':'',
			'descripcion_ruso':'',
			'descripcion_portuges':''
		}	

	if lugar.fecha_de_creacion != "":
		fecha_de_creacion = lugar.fecha_de_creacion.strftime("%Y-%m-%d")
		
	context = {
		'id' : lugar.id,
		'nombre_arabe':lugar.nombre.nombre_arabe,
		'nombre_chino':lugar.nombre.nombre_chino,
		'nombre_espanol':lugar.nombre.nombre_espanol,
		'nombre_frances':lugar.nombre.nombre_frances,
		'nombre_ingles':lugar.nombre.nombre_ingles,
		'nombre_ruso':lugar.nombre.nombre_ruso,
		'nombre_portuges':lugar.nombre.nombre_portuges,
		'descripcion_arabe':descripcion['descripcion_arabe'],
		'descripcion_chino':descripcion['descripcion_chino'],
		'descripcion_espanol':descripcion['descripcion_espanol'],
		'descripcion_frances':descripcion['descripcion_frances'],
		'descripcion_ingles':descripcion['descripcion_ingles'],
		'descripcion_ruso':descripcion['descripcion_ruso'],
		'descripcion_portuges':descripcion['descripcion_portuges'],
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

	return context

def obtenerTodosLugares(request):
	features = []
	lugares= Lugar.objects.all()
	descripcion = ""
	fecha_de_creacion = ""
	portada = "";
	icono = "";

	for lugar in lugares:

		if lugar.descripcion is not None and lugar.descripcion.descripcion_espanol != "":
			descripcion = lugar.descripcion.descripcion_espanol

		if lugar.icono is not None and lugar.icono != "":
			icono = lugar.icono

		if lugar.portada is not None and lugar.portada != "":
			portada = lugar.portada

		if lugar.fecha_de_creacion != "":
			fecha_de_creacion = lugar.fecha_de_creacion.strftime("%Y-%m-%d")

		features.append(
			{
				"type": "Feature",
				"properties": {
					"id": lugar.id,
					"name": lugar.nombre.nombre_espanol,
					"descripcion" : descripcion,
					"categoria_id" : lugar.categoria_id,
					"ciudad" : lugar.ciudad,
					"direccion" : lugar.direccion,
					"icono" : icono,
					"portada" : portada,
					"sitio_web" : lugar.sitio_web,
					"redes_sociales" : lugar.redes_sociales,
					"fecha_de_creacion" : fecha_de_creacion,
					"tags" : lugar.tags,
				},
				"geometry": {
					"type": "Point",
					"coordinates": [lugar.location.longtitude, lugar.location.latitude]					
				},
			}
		)



	context = {
		"type": "FeatureCollection",
		"features": features
	}

	return context

def deletePlace(request):
	lugar_id = request.POST.get('id')
	lugar = Lugar.objects.get(pk=lugar_id);
	lugar.delete()
	return True
