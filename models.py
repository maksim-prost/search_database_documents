from __init__ import db

class FileStorage(db.Model):
	"""docstring for FileStorage"""
	id = db.Column(db.Integer, primary_key=True)
	filename = db.Column(db.String(150), unique=True)

	def save(self):
	# cохранит запись в таблице
		db.session.add(self)
		db.session.commit()


# db.create_all() #при первом запуске, для создания таблиц бд
