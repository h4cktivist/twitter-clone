function openMenu(){
	document.getElementById("user_menu").classList.toggle('active');
	document.getElementById("form_block").classList.toggle('active');
	document.getElementById("post_block").classList.toggle('active');
	document.getElementById("poloska").classList.toggle('active');
	document.getElementById("user_trends").classList.toggle('active');
	document.getElementById("menu_btn").classList.toggle('active');
	document.getElementById("user_info").classList.toggle('active');
	document.getElementById("user_info_name").classList.toggle('active');
	document.getElementById("switcher_box").classList.toggle('active');
}

function openLowSizeMenu(){
	document.getElementById("menu_lowsize").classList.toggle('active');
	document.getElementById('form_create_post_lowsize').classList.toggle('active');
	document.getElementById('txtarea').classList.toggle('lowsize');
	document.getElementById('switcher_box_lowsize').classList.toggle('active');
}