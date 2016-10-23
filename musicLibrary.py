import os
import sqlite3
import eyed3
import model.musicLibraryRepository as repository
from model.mp3 import *

from song import *

#_dbName = 'mp3Library.db'
#_musicPath = "/{0}".format(os.path.join("","home","kechunet","Music"))
_musicPath = "/{0}".format(os.path.join("","home","kechusoft","Music"))
#_musicPath = os.path.join("C:/", "Users","nkinaschuk","Music")

def getMp3InMusic():
	os.listdir(_musicPath)
	mp3Files = [(eyed3.load(os.path.join(_musicPath, mp3)), mp3)
		for mp3 in os.listdir(_musicPath) if mp3.endswith(".mp3")]
	return mp3Files

def saveMp3s():
	mp3Files = getMp3InMusic()

	mp3s = [Mp3(title=mp3File[0].tag.title,
			artist=mp3File[0].tag.artist,
			fileName=mp3File[1],
			path=_musicPath) for mp3File in mp3Files]

	repository.insertMp3s(mp3s)


def getMp3s():
	mp3s = repository.getAllMp3s()
	return [Song(mp3.mp3Id,mp3.title, mp3.artist) for mp3 in mp3s]

def getMp3ById(mp3Id):
	mp3 = repository.getMp3ById(mp3Id)
	return mp3

def startNewCurrentPlaylist(mp3Id):
	repository.startNewCurrentPlaylist(mp3Id)

def enqueueInCurrentPlaylist(mp3Id):
	repository.enqueueInCurrentPlaylist(mp3Id)