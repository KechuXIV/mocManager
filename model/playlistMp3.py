from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base
from context import Base


class PlaylistMp3(Base):
	__tablename__ = 'playlistsMp3s'
	playlistId = Column(Integer, primary_key=True)
	mp3Id = Column(Integer)
	position = Column(Integer)

	def __repr__(self):
		return "<PlaylistMp3(playlistId='%s', \
			mp3Id='%s', \
			position='%s')>" % (self.playlistId, 
					self.mp3Id, 
					self.position)
