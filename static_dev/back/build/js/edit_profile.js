$(document).ready(function() {
	moment.locale('es');
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