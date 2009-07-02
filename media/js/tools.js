function contentLoad(url,content){

	content.html("<div class='loader center' style='width: 100px;'><span>Cargando...</span></div>");

	content.load(url,{},function(responseText, textStatus, XMLHttpRequest) {
		if ( XMLHttpRequest.status != 200 )
			alert('Ups... un error ocurrió en el servidor: '+XMLHttpRequest.status);
		});

	return false;
}


function processStatus(s){

	if ( s == 200 )
		return true;
	
	return false;
}

function showErrors(errors){
	$('.errors').html(errors);
	$('.errors').show();
}

function unShowErrors(){
	$('.errors').hide();
}
