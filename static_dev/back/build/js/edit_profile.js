$(document).ready(function() {
	moment.locale('es');
	var fecha = $('#id_fecha_de_nac').val();
	console.log(fecha);


	
	var fecha = $('#id_fecha_de_nac').val().replace('de ','');
	fecha = fecha.replace(' de','');
	$('#id_fecha_de_nac').val(fecha);
	
	$('#id_fecha_de_nac').daterangepicker({
		locale: {
			format: 'DD MMMM YYYY'
		},
		singleDatePicker: true,
		calender_style: "picker_4"
	}, function(start, end, label) {
		//console.log(start.toISOString(), end.toISOString(), label);
	});
});