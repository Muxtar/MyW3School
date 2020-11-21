var leftMenu = document.getElementById('left_menu');
var mainMenu = document.getElementById('main_menu');
var newMenu = document.getElementById('new-menu');

var left = window.getComputedStyle(leftMenu);

function test(){
	if(window.innerWidth <= 1500){
		if(left.getPropertyValue('visibility') == 'hidden'){
			leftMenu.style.visibility = 'visible';	
		}

		else{
			leftMenu.style.visibility = 'hidden';	
		}
	}
}

function test2(){
	console.log(window.innerWidth);
	if(window.innerWidth <= 1500){
		if(left.getPropertyValue('visibility') == 'visible'){
			leftMenu.style.visibility = 'hidden';
		}
	}
}

window.onresize = function(){
	if(window.innerWidth > 1500){
		leftMenu.style.visibility = 'visible';
	}
}
