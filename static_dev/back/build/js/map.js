
var map, GeoMarker, infoWindow;

var contents = '<div class="" role="tabpanel" data-example-id="togglable-tabs">';
	contents += '<div class="col-md-12 col-sm-12 col-xs-12">';
	contents += '<h2 id="title"> Nuevo Lugar </h2><br />';	
	contents += '<form class="form-horizontal form-label-left" onsubmit="actualizarLugar($(this))">';	
	contents += '<ul id="myTab" class="nav nav-tabs bar_tabs" role="tablist">';
	contents += '<li role="presentation" class="active"><a href="#tab_español" id="home-tab" role="tab" data-toggle="tab" aria-expanded="true">Español</a>';
	contents += '</li>';
	contents += '<li role="presentation" class=""><a href="#tab_ingles" role="tab" id="profile-tab" data-toggle="tab" aria-expanded="false">Inglés</a>';
	contents += '</li>';
	contents += '</ul>';
	contents += '<div id="myTabContent" class="tab-content">';
	contents += '<div role="tabpanel" class="tab-pane fade active in" id="tab_español" aria-labelledby="home-tab">';
	
	contents += '<input id="id" name="id" class="form-control" type="hidden" placeholder="Id" />';
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
	contents += '<input id="latitud" name="latitud" class="form-control" type="hidden" placeholder="Latitud" />';
	contents += '<input id="longitud" name="longitud" class="form-control" type="hidden" placeholder="Longitud" />';
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
	contents += '<button type="button" class="btn btn-danger">Cancelar</button>';
	contents += '<button type="submit" class="btn btn-success">Guardar</button>';
	contents += '</div>';
	contents += '</div>';

	contents += '</div>';
	contents += '<div role="tabpanel" class="tab-pane fade" id="tab_ingles" aria-labelledby="profile-tab">';
	contents += '<div class="form-group">';
	contents += '<label class="col-xs-3 control-label">Name: </label>';
	contents += '<div class="col-xs-9">';
	contents += '<input id="nombre_ingles" name="nombre_ingles" class="form-control" type="text" placeholder="Name" />';
	contents += '</div>';
	contents += '</div>';	
	contents += '<div class="form-group">';
	contents += '<label class="col-xs-3 control-label">Description: </label>';
	contents += '<div class="col-xs-9">';
	contents += '<textarea id="descripcion_ingles" name="descripcion_ingles" class="form-control" placeholder="Description"></textarea>';
	contents += '</div>';
	contents += '</div>';
	contents += '<div class="ln_solid"></div>';
	contents +=	'<div class="form-group">';
	contents +=	'<div class="col-xs-6 col-xs-offset-6">';
	contents += '<button type="button" class="btn btn-danger">Delete</button>';
	contents += '<button type="submit" class="btn btn-success">Save</button>';
	contents += '</div>';
	contents += '</div>';
	contents += '</div>';
	contents += '</div>';
	contents += '</div>';

	contents += '</form>';
	contents += '</div>';
	contents += '</div>';

	//quitar scroll bar info windows maps
	contents = '<div class="scrollFix">'+contents+'</div>';

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
	map.data.loadGeoJson('/plataforma/mostrar_lugares/');
	
	infoWindow = new google.maps.InfoWindow({
    	minWidth: 600
  	});

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
			cargarFormularioLugar(data.id, data.nombre_espanol, data.nombre_ingles, '', data.latitude, data.longtitude, '', '', 
				'', '','')

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
			cargarFormularioLugar(data.id, data.nombre_espanol, data.nombre_ingles, data.direccion, data.latitude, data.longtitude, data.icono, data.portada, data.descripcion_español, data.descripcion_ingles, data.sitio_web);

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
			cargarFormularioLugar(data.id, data.nombre_espanol, data.nombre_ingles, data.direccion, data.latitude, data.longtitude, data.icono, data.portada, data.descripcion_español, data.descripcion_ingles, data.sitio_web);
		},
		error : function(xhr,errmsg,err) {
			
			console.log(xhr.status + ": " + xhr.responseText);
		}
	});

}

function cargarFormularioLugar(id, nombre, nombre_ingles, direccion, latitud, longitud, icono, portada, descripcion, descripcion_ingles, sitio_web){
	
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
	$('#nombre_ingles').val(nombre_ingles);
	$('#descripcion_ingles').val(descripcion_ingles);
}

function error(){
	new PNotify({
		title: '¡Oh No!',
		text: 'Acaba de ocurrir un error',
		type: 'error',
		styling: 'bootstrap3'
	});
}

