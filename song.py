class Song(object):
	def __init__(self, rowId, title, artist):
		self.rowId = rowId
		self.title = title
		self.artist = artist

	def __str__(self):
		return "({0}, {1} - {2})".format(self.rowId,
			self.artist, self.title)
