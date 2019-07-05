from __init__ import app, db
from flask import  render_template,request
from models import FileStorage
from search_by_doc import find_text_in_dirs

@app.route('/',methods=['POST','GET'])
def index():
	list_save_doc = [file.filename for file in FileStorage.query.all()]
	if request.method=='POST':
		file = request.files.get('file')
		if not file:
			return  'error loading file', 204
		filename = app.config['DIR_SAVE_FILES'] + file.filename.split('/')[-1]
		
		if filename in list_save_doc:
			return  'error, a document with the same name exists', 208
		
		file.save(filename)
		FileStorage(filename=filename).save()
		return '% s \n success upload'%file.filename, 202
	
	result_search={}
	find = request.args.get('search')
	if find:
		result_search = find_text_in_dirs(find, list_save_doc)
	return render_template('index.html',result_search=result_search,find=find)

	

app.run()
