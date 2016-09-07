class Song(object):
	def __init__(self, rowId, name, title):
		self.rowId = rowId
		self.artist = artist
		self.title = title

	def __str__(self):
		return "({0}, {1} - {3})".format(self.rowId,
			self.name, self.title)
