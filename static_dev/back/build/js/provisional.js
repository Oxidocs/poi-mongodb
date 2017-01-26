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