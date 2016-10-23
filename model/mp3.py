from sqlalchemy import *
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from playlistMp3 import *
from context import Base


class Mp3(Base):
	__tablename__ = 'mp3s'
	mp3Id = Column(Integer, primary_key=True)
	title = Column(String(50))
	artist = Column(String(50))
	fileName = Column(String(50))
	path = Column(String(250))

	playlists = relationship('Playlist',
						secondary='playlistsMp3s',
						back_populates='mp3s')

	def __init__(self, title, artist, fileName, path, mp3Id=None):
		self.title = title
		self.artist = artist
		self.fileName = fileName
		self.path = path
		self.mp3Id = mp3Id

	def __repr__(self):
		return "<Mp3(mp3Id='%s', \
			title='%s', \
			artist='%s', \
			fileName='%s', \
			path='%s')>" % (self.mp3Id, 
					self.title, 
					self.artist, 
					self.fileName, 
					self.path)