from sqlalchemy import *
from context import engine, Session
from mp3 import *
from sqlalchemy.sql import func
from playlist import *
from playlistMp3 import *


_currentPlaylistId = 0

def getAllMp3s():
	return Session().query(Mp3)

def getMp3ById(mp3Id):
	return Session().query(Mp3).filter_by(mp3Id=mp3Id).first()

def insertMp3s(mp3s):
	session = Session()
	session.add_all(mp3s)
	session.commit()

def insertPlaylists(playlists):
	session = Session()
	session.add_all(playlists)
	session.commit()

def instertMp3sInPlaylists(mp3, playlist):
	session = Session()
	session.add_all(playlists)
	session.commit()

def startNewCurrentPlaylist(mp3Id):
	session = Session()
	session.query(PlaylistMp3s).filter_by(playlistId=_currentPlaylistId).delete()
	playlistMp3 = PlaylistMp3(mp3Id=mp3Id, playlistId= _currentPlaylistId, position=1)
	session.add(playlistMp3)
	session.commit()

def enqueueInCurrentPlaylist(mp3Id):
	session = Session()
	position = session.query(func.max(PlaylistMp3.position))
		.filter_by(playlistId=0).first()[0]
	playlistMp3 = PlaylistMp3(mp3Id=mp3Id, playlistId = _currentPlaylistId, position=position)
	session.add(playlistMp3)
	session.commit()
