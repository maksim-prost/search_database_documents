from docxtpl import Document
import os

def find_text_in_doc(find,doc):
	#точное вхождение искомой строки выделяется цветом
	# без учета регистра добавляется в результат поиска
	return [par.text.replace(find, '<span class="find">%s</span>'%find) 
		for par in Document(doc).paragraphs if find.lower() in par.text.lower()]

def find_text_in_dir(find, name_dir):
	result_find = {}
	for doc in os.listdir(name_dir):
		if doc.endswith('.docx'):
			list_find = find_text_in_doc(find, name_dir+doc)
			if list_find:
				result_find[doc] = list_find
	return result_find

def find_text_in_dirs(find, list_dirs):
	"""
	перебор файлов из списка(соответсвует файлам в бд и поиск в них искомой строки
	по параграфам, возвращаются параграфы
	работает только с .docх (пока)
	"""
	result_find = {}
	for doc in list_dirs:
		if doc.endswith('.docx'):
			list_find = find_text_in_doc(find, doc)
			if list_find:
				result_find[doc.split('/')[-1]] = list_find
	return result_find


