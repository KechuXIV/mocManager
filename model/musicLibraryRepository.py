from sqlalchemy import *
from context import engine, Session
from mp3 import *
from playlist import *
from playlistMp3 import *


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