from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base
from context import Base


class Mp3(Base):
	__tablename__ = 'mp3s'
	mp3Id = Column(Integer, primary_key=True)
	title = Column(String(50))
	artist = Column(String(50))
	fileName = Column(String(50))
	path = Column(String(250))

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