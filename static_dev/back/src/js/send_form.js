$('form.send').on('submit', function(event){
	event.preventDefault();
	var url = $(this).attr('action');
	if (url==null) url = window.location.href

	var csrftoken = getCookie('csrftoken');
	var data = new FormData($(this).get(0));

	$.ajax({
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
});