
var map, GeoMarker, infoWindow;

var contents = '<h4 id="title" class="text-center">Nuevo Lugar</h4>';
	contents += '<div class="ln_solid"></div>';
	contents += '<form class="form-horizontal form-label-left" onsubmit="actualizarLugar($(this))">';
	/*contents += '<div class="form-group">';
	contents += '<label class="col-xs-3 control-label">Id: </label>';
	contents += '<div class="col-xs-9">';*/
	contents += '<input id="id" name="id" class="form-control" type="hidden" placeholder="Id" />';
	/*contents += '</div>';
	contents += '</div>';*/
	contents += '<div class="form-group">';
	contents += '<label class="col-xs-3 control-label">Nombre: </label>';
	contents += '<div class="col-xs-9">';
	contents += '<input id="nombre" name="nombre" class="form-control" type="text" placeholder="Nombre" />';
	contents += '</div>';
	contents += '</div>';
	contents += '<div class="form-group">';
	contents += '<label class="col-xs-3 control-label">Dirección: </label>';
	contents += '<div class="col-xs-9">';
	contents += '<input id="direccion" name="direccion" class="form-control" type="text" placeholder="Dirección" />';
	contents += '</div>';
	contents += '</div>';
	/*contents += '<div class="form-group">';
	contents += '<label class="col-xs-3 control-label">Latitud: </label>';
	contents += '<div class="col-xs-9">';*/
	contents += '<input id="latitud" name="latitud" class="form-control" type="hidden" placeholder="Latitud" />';
	/*contents += '</div>';
	contents += '</div>';*/
	/*contents += '<div class="form-group">';
	contents += '<label class="col-xs-3 control-label">Longitud: </label>';
	contents += '<div class="col-xs-9">';*/
	contents += '<input id="longitud" name="longitud" class="form-control" type="hidden" placeholder="Longitud" />';
	/*contents += '</div>';
	contents += '</div>';*/
	contents += '<div class="form-group">';
	contents += '<label class="col-xs-3 control-label">Icono: </label>';
	contents += '<div class="col-xs-9">';
	contents += '<input id="icono" name="icono" class="form-control" type="file" placeholder="Icono" />';
	contents += '</div>';
	contents += '</div>';
	contents += '<div class="form-group">';
	contents += '<label class="col-xs-3 control-label">Portada: </label>';
	contents += '<div class="col-xs-9">';
	contents += '<input id="portada" name="portada" class="form-control" type="file" placeholder="Portada" />';
	contents += '</div>';
	contents += '</div>';
	contents += '<div class="form-group">';
	contents += '<label class="col-xs-3 control-label">Descripción: </label>';
	contents += '<div class="col-xs-9">';
	contents += '<textarea id="descripcion" name="descripcion" class="form-control" placeholder="Descripción"></textarea>';
	contents += '</div>';
	contents += '</div>';
	contents += '<div class="form-group">';
	contents += '<label class="col-xs-3 control-label">Sitio Web: </label>';
	contents += '<div class="col-xs-9">';
	contents += '<input id="sitio_web" name="sitio_web" class="form-control" type="text" placeholder="Sitio Web" />';
	contents += '</div>';
	contents += '</div>';
	contents += '<div class="ln_solid"></div>';
	contents +=	'<div class="form-group">';
	contents +=	'<div class="col-xs-6 col-xs-offset-6">';
	contents += '<button type="button" class="btn btn-primary">Cancelar</button>';
	contents += '<button type="submit" class="btn btn-success">Guardar</button>';
	contents += '</div>';
	contents += '</div>';
	contents += '</form>';

function initialize() {

	var mapOptions = {
		zoomControl: true,
		mapTypeControl: true,
		scaleControl: true,
		streetViewControl: true,
		rotateControl: true,
		zoom: 10,
		center: new google.maps.LatLng(0,0),
		mapTypeId: google.maps.MapTypeId.ROADMAP
	};

	map = new google.maps.Map(document.getElementById('map'), mapOptions);	
	map.data.loadGeoJson('http://localhost:3000/plataforma/mostrar_lugares/');
	
	infoWindow = new google.maps.InfoWindow();

	map.data.addListener('click', function(event) {
		infoWindow.setContent(contents);
		infoWindow.setPosition(event.feature.getGeometry().get());
		infoWindow.setOptions({pixelOffset: new google.maps.Size(0,-30)});
		infoWindow.open(map);
		cargarLugares(event.feature.getProperty('id'));
	});  

	GeoMarker = new GeolocationMarker();
	GeoMarker.setCircleOptions({fillColor: '#808080'});

	google.maps.event.addListenerOnce(GeoMarker, 'position_changed', function() {
		map.setCenter(this.getPosition());
		map.fitBounds(this.getBounds());
	});

	google.maps.event.addListener(GeoMarker, 'geolocation_error', function(e) {
		alert('Ocurrió un error obteniendo tu posición. Mensaje: ' + e.message);
	});

	GeoMarker.setMap(map);

	var drawingManager = new google.maps.drawing.DrawingManager({
		drawingMode: google.maps.drawing.OverlayType.MARKER,
		drawingControl: true,
		drawingControlOptions: {
			position: google.maps.ControlPosition.TOP_CENTER,
			drawingModes: [
				google.maps.drawing.OverlayType.MARKER,
				// google.maps.drawing.OverlayType.CIRCLE,
				// google.maps.drawing.OverlayType.POLYGON,
				google.maps.drawing.OverlayType.POLYLINE,
				// google.maps.drawing.OverlayType.RECTANGLE
			]
		},
		markerOptions: {
			// icon: '/media/map/geolocation_marker.png',
			// draggable: true,
			// clickable: true,
		},
		circleOptions: {
			fillColor: '#ffff00',
			fillOpacity: 1,
			strokeWeight: 5,
			clickable: false,
			editable: true,
			zIndex: 1
		}
	});

	drawingManager.setMap(map);

	google.maps.event.addDomListener(drawingManager,'markercomplete', function(marker) {
		crearMarcador(marker);
	});
}

google.maps.event.addDomListener(window, 'load', initialize);

if(!navigator.geolocation) {
	alert('Tu navegador no soporta geolocalización');
}

function crearMarcador(marker) {

	var lat = marker.position.lat();
	var long = marker.position.lng();

	var myLatlng = new google.maps.LatLng(lat,long);
	var marker_created = new google.maps.Marker({
			position: myLatlng,
			draggable:true,
	});

	guardarLugar(lat,long, marker_created);

	marker.setMap(null);
	marker_created.setMap(map);

	infoWindow.setContent(contents);
	infoWindow.setOptions({pixelOffset: new google.maps.Size(0,10)});
	infoWindow.open(map, marker_created);

	marker_created.addListener('click', function() {
		console.log(marker_created);
		infoWindow.setContent(contents);
		infoWindow.setOptions({pixelOffset: new google.maps.Size(0,10)});
		infoWindow.open(map, marker_created);
		cargarLugares(marker_created.data_marker.id);
	});
}

function guardarLugar(lat, long, marker){
	event.preventDefault();
	var csrftoken = getCookie('csrftoken');
	var url = '/plataforma/guardar_lugar/';

	$.ajax({
		url : url,
		type : "POST",
		data : { lat : lat, long: long },

		beforeSend: function(xhr, settings) {
			if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
				xhr.setRequestHeader("X-CSRFToken", csrftoken);
			}
		},
		success : function(data) {

			marker.set("data_marker", data);
			cargarFormularioLugar(data.id, data.nombre, '', data.latitude, data.longtitude, '', '', 
				'', '')

			new PNotify({
				title: 'Guardado',
				text: 'Se han realizado los cambios exitosamente',
				type: 'success',
				styling: 'bootstrap3'
			});
		},
		error : function(xhr,errmsg,err) {
			error();
			console.log(xhr.status + ": " + xhr.responseText);
		}
	});
}

function actualizarLugar(form){
	event.preventDefault();
	var csrftoken = getCookie('csrftoken');
	var url = '/plataforma/guardar_lugar/';
	var data = new FormData(form.get(0));

	$.ajax({
		url : url,
		type : "POST",
		data: data,
		cache: false,
		contentType: false,
		processData: false,
		type: 'POST',

		beforeSend: function(xhr, settings) {
			if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
				xhr.setRequestHeader("X-CSRFToken", csrftoken);
			}
		},
		success : function(data) {

			console.log(data);
			cargarFormularioLugar(data.id, data.nombre, data.direccion, data.latitude, data.longtitude, data.icono, data.portada, data.descripcion, data.sitio_web);

			new PNotify({
				title: 'Guardado',
				text: 'Se han realizado los cambios exitosamente',
				type: 'success',
				styling: 'bootstrap3'
			});
		},
		error : function(xhr,errmsg,err) {
			error();
			console.log(xhr.status + ": " + xhr.responseText);
		}
	});
}

function mostrarLugar(){

}

function cargarLugares(id){

	event.preventDefault();
	var csrftoken = getCookie('csrftoken');
	var url = '/plataforma/mostrar_lugar/';

	$.ajax({
		url : url,
		type : "POST",
		data : { id : id },

		beforeSend: function(xhr, settings) {

			if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
				xhr.setRequestHeader("X-CSRFToken", csrftoken);
			}
		},
		success : function(data) {
			console.log(data);
			cargarFormularioLugar(data.id, data.nombre, data.direccion, data.latitude, data.longtitude, data.icono, data.portada, data.descripcion, data.sitio_web);
		},
		error : function(xhr,errmsg,err) {
			
			console.log(xhr.status + ": " + xhr.responseText);
		}
	});

}

function cargarFormularioLugar(id, nombre, direccion, latitud, longitud, icono, portada, descripcion, sitio_web){
	
	$('#id').val(id);
	$('#title').text(nombre);
	$('#nombre').val(nombre);
	$('#direccion').val(direccion);
	$('#latitud').val(latitud);
	$('#longitud').val(longitud);
	$('#icono').val(icono);
	$('#portada').val(portada);
	$('#descripcion').val(descripcion);
	$('#sitio_web').val(sitio_web);

}

function error(){
	new PNotify({
		title: '¡Oh No!',
		text: 'Acaba de ocurrir un error',
		type: 'error',
		styling: 'bootstrap3'
	});
}

