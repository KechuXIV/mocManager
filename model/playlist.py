from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base
from context import Base


class Playlist(Base):
	__tablename__ = 'playlists'
	playlistId = Column(Integer, primary_key=True)
	name = Column(String(50))
	description = Column(String(50))

	def __repr__(self):
		return "<Playlist(playlistId='%s', \
			name='%s', \
			description='%s')>" % (self.playlistId, 
					self.name, 
					self.description)
