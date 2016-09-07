class Song(object):
	"""docstring for Song"""
	def __init__(self, rowId, name):
		self.rowId = rowId
		self.name = name

	def __str__(self):
		return "({0}, {1})".format(self.rowId, self.name)

#	def __repr__(self):
#		return str(self)