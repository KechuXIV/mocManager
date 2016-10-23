from sqlalchemy import *
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from context import Base


class PlaylistMp3(Base):
	__tablename__ = 'playlistsMp3s'
	playlistId = Column(Integer, ForeignKey('playlists.playlistId'), primary_key=True)
	mp3Id = Column(Integer, ForeignKey('mp3s.mp3Id'), primary_key=True)
	position = Column(Integer)

	def __init__(self, playlistId, mp3Id, position):
		self.playlistId = playlistId
		self.mp3Id = mp3Id
		self.position = position

	def __repr__(self):
		return "<PlaylistMp3(playlistId='%s', \
			mp3Id='%s', \
			position='%s')>" % (self.playlistId, 
					self.mp3Id, 
					self.position)
