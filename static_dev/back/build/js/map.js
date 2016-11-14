
var map, GeoMarker, infoWindow;

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
	infoWindow = new google.maps.InfoWindow();

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

	guardarLugar(lat,long);

	var myLatlng = new google.maps.LatLng(lat,long);
	var marker_created = new google.maps.Marker({
			position: myLatlng,
			draggable:true,
	});

	marker.setMap(null);
	marker_created.setMap(map);

	var contents = '<h4 class="text-center">Nuevo Lugar</h4>';
	contents += '<div class="ln_solid"></div>';
	contents += '<form class="form-horizontal form-label-left">';
	contents += '<div class="form-group">';
	contents += '<label class="col-xs-3 control-label">Nombre: </label>';
	contents += '<div class="col-xs-9">';
	contents += '<input class="form-control" type="text" placeholder="Nombre" />';
	contents += '</div>';
	contents += '</div>';
	contents += '<div class="form-group">';
	contents += '<label class="col-xs-3 control-label">Dirección: </label>';
	contents += '<div class="col-xs-9">';
	contents += '<input class="form-control" type="text" placeholder="Dirección" />';
	contents += '</div>';
	contents += '</div>';
	contents += '<div class="form-group">';
	contents += '<label class="col-xs-3 control-label">Latitud: </label>';
	contents += '<div class="col-xs-9">';
	contents += '<input class="form-control" type="text" placeholder="Latitud" />';
	contents += '</div>';
	contents += '</div>';
	contents += '<div class="form-group">';
	contents += '<label class="col-xs-3 control-label">Longitud: </label>';
	contents += '<div class="col-xs-9">';
	contents += '<input class="form-control" type="text" placeholder="Longitud" />';
	contents += '</div>';
	contents += '</div>';
	contents += '<div class="form-group">';
	contents += '<label class="col-xs-3 control-label">Icono: </label>';
	contents += '<div class="col-xs-9">';
	contents += '<input class="form-control" type="file" placeholder="Icono" />';
	contents += '</div>';
	contents += '</div>';
	contents += '<div class="form-group">';
	contents += '<label class="col-xs-3 control-label">Portada: </label>';
	contents += '<div class="col-xs-9">';
	contents += '<input class="form-control" type="file" placeholder="Portada" />';
	contents += '</div>';
	contents += '</div>';
	contents += '<div class="form-group">';
	contents += '<label class="col-xs-3 control-label">Descripción: </label>';
	contents += '<div class="col-xs-9">';
	contents += '<textarea class="form-control" placeholder="Descripción"></textarea>';
	contents += '</div>';
	contents += '</div>';
	contents += '<div class="form-group">';
	contents += '<label class="col-xs-3 control-label">Sitio Web: </label>';
	contents += '<div class="col-xs-9">';
	contents += '<input class="form-control" type="text" placeholder="Sitio Web" />';
	contents += '</div>';
	contents += '</div>';
	contents += '<div class="ln_solid"></div>';
	contents +=	'<div class="form-group">';
	contents +=	'<div class="col-xs-6 col-xs-offset-6">';
	contents += '<button type="reset" class="btn btn-primary">Cancelar</button>';
	contents += '<button type="submit" class="btn btn-success">Guardar</button>';
	contents += '</div>';
	contents += '</div>';
	contents += '</form>';

	infoWindow.setContent(contents);
	infoWindow.open(map, marker_created);

	marker_created.addListener('click', function() {
		var contents = 'Hello World';
		infoWindow.setContent(contents);
		infoWindow.open(map, marker_created);
	});
}

function guardarLugar(lat, long){
	event.preventDefault();
	var csrftoken = getCookie('csrftoken');
	var url = '/plataforma/guardar_lugar/';

	$.ajax({
		url : url,
		type : "POST",
		data : { lat : lat, long: long },

		beforeSend: function(xhr, settings) {
			new PNotify({
				title: 'Guardando',
				text: 'Guardando los cambios',
				type: 'info',
				styling: 'bootstrap3'
			});
			if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
				xhr.setRequestHeader("X-CSRFToken", csrftoken);
			}
		},
		success : function(data) {

			console.log(data);

			new PNotify({
				title: 'Guardado',
				text: 'Se han realizado los cambios exitosamente',
				type: 'success',
				styling: 'bootstrap3'
			});
		},
		error : function(xhr,errmsg,err) {
			new PNotify({
				title: '¡Oh No!',
				text: 'Acaba de ocurrir un error',
				type: 'error',
				styling: 'bootstrap3'
			});
			console.log(xhr.status + ": " + xhr.responseText);
		}
	});
}
