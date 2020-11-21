var divSigin = document.getElementById('sigin');
var divLogin = document.getElementById('login');
var notifaction = document.getElementById('notifaction');


function change(param){
	if(param.attributes[0].value == 'title-sigin'){
		divLogin.style.display = 'none';
		divSigin.style.display = 'block';
		notifaction.innerHTML = "";
	}

	else{
		divLogin.style.display = 'block';
		divSigin.style.display = 'none';
		notifaction.innerHTML = "";
	}
			
}
