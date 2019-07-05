
// выбрать элемент "кнопка загрузить" по id, и к событию
// onclick прикрепить функцию, отправляющию файл на сервер 
uploadFiles = document.querySelector('#file-upload')
uploadFiles.onclick = function(){
	console.log('click')
	file = document.querySelector('#file')
	if (file.value != ''){
		form =document.querySelector('#uploadForm')
		console.log(form)
		console.log(form.action)
		request('POST', new FormData(form), form.action)
		file.value = ''
	}
}

function request(method,form,url) {
	r = new XMLHttpRequest();
	r.open(method,url,true);
	r.onload = function(){
		alert(r.responseText)
	}
	r.send(form);
}