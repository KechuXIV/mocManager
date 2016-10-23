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

def getPlaylistLastPosition(playlistId):
	session = Session()
	lastPosition = int(session.query(func.max(PlaylistMp3.position)).filter_by(playlistId=playlistId).first()[0])
	session.close()
	return lastPosition

def insertMp3s(mp3s):
	session = Session()
	session.add_all(mp3s)
	session.commit()

def insertPlaylists(playlists):
	session = Session()
	session.add_all(playlists)
	session.commit()

def instertMp3sInPlaylists(mp3Id, playlistId, position=None):
	session = Session()
	if(position is None):
		position = getPlaylistLastPosition(playlistId) + 1
	playlist = Playlist(mp3Id, playlistId, position)
	session.add_all(playlist)
	session.commit()

def startNewCurrentPlaylist(mp3Id):
	session = Session()
	session.query(PlaylistMp3s).filter_by(playlistId=_currentPlaylistId).delete()
	playlistMp3 = PlaylistMp3(mp3Id, _currentPlaylistId, 1)
	session.add(playlistMp3)
	session.commit()

def enqueueInCurrentPlaylist(mp3Id):
	session = Session()
	lastPosition = getPlaylistLastPosition(_currentPlaylistId)
	playlistMp3 = PlaylistMp3(mp3Id, _currentPlaylistId, lastPosition + 1)
	session.add(playlistMp3)
	session.commit()

def createPlaylist(name, description):
	session = Session()
	playlist = Playlist(name, description)
	session.add(playlist)
	session.commit()