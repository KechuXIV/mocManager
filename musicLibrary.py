import os
import sqlite3
import eyed3
from song import *

_dbName = 'mp3Library.db'
#_musicPath = "/{0}".format(os.path.join("","home","kechunet","Music"))
#_musicPath = "/{0}".format(os.path.join("","home","kechusoft","Music"))
_musicPath = os.path.join("C:/", "Users","nkinaschuk","Music")

def createDatabase():
	connection = sqlite3.connect(_dbName)
	try:
		cursor = connection.cursor()

		cursor.execute("CREATE TABLE mp3s "
			"(title text, artist text, fileName text, path text)")
	except Exception, e:
		raise
	finally:
		connection.close()

def getMp3InMusic():
	os.listdir(_musicPath)
	mp3Files = [file for file in os.listdir(_musicPath) if file.endswith(".mp3")]
	return mp3Files

def saveMp3s():
	connection = sqlite3.connect(_dbName)

	try:
		cursor = connection.cursor()

		mp3Files = getMp3InMusic()

		for mp3File in mp3Files:

			mp3Info = eyed3.load(os.path.join(_musicPath, mp3File))

			value = (mp3Info.tag.title,
				mp3Info.tag.artist,
				mp3File,
				_musicPath)

			cursor.execute("INSERT INTO mp3s "
				"VALUES "
				"(?, ?, ?, ?)",
				value)

		connection.commit()
	except Exception, e:
		raise
	finally:
		connection.close()

def getMp3s():
	connection = sqlite3.connect(_dbName)

	try:
		cursor = connection.cursor()
		cursor.execute("SELECT rowid, title, artist "
			"FROM mp3s")

		mp3s = cursor.fetchall()
	except Exception, e:
		raise
	finally:
		connection.close()

	songs = []
	for mp3 in mp3s:
		songs.append(Song(mp3[0],mp3[1], mp3[2]))

	return songs

def getMp3ById(id):
	connection = sqlite3.connect(_dbName)

	try:
		cursor = connection.cursor()
		rowId = (id,)

		cursor.execute("SELECT fileName "
				"FROM "
				"mp3s "
				"WHERE "
				"rowId = ? ", rowId)

		mp3Name = cursor.fetchone()[0]

		return os.path.join(_musicPath, mp3Name)
	except Exception, e:
		raise
	finally:
		connection.close()
