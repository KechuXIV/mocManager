import os
import sqlite3
from song import *

_dbName = 'mp3Library.db'
#_musicPath = "/{0}".format(os.path.join("","home","kechunet","Music"))
#_musicPath = "/{0}".format(os.path.join("","home","kechusoft","Music"))
_musicPath = os.path.join("C:/", "Users","nkinaschuk","Music")

def createDatabase():
	connection = _getConnection()
	try:
		cursor = _getCursor(connection)

		cursor.execute("CREATE TABLE mp3s "
			"(name text, path text)")
	except Exception, e:
		raise
	finally:
		connection.close()

def getMp3InMusic():
	os.listdir(_musicPath)
	mp3Files = [file for file in os.listdir(_musicPath) if file.endswith(".mp3")]
	return mp3Files

def saveMp3s():
	connection = _getConnection()

	try:
		cursor = _getCursor(connection)

		mp3Files = getMp3InMusic()

		for mp3File in mp3Files:

			value = (_sanitizeString(mp3File), _sanitizeString(_musicPath))

			cursor.execute("INSERT INTO mp3s "
				"VALUES "
				"(?, ?)",value)

		connection.commit()
	except Exception, e:
		raise
	finally:
		connection.close()

def getMp3s():
	connection = _getConnection()

	try:
		cursor = _getCursor(connection)
		cursor.execute("SELECT rowId, name "
				"FROM "
				"mp3s ")

		mp3s = cursor.fetchall()
	except Exception, e:
		raise
	finally:
		connection.close()

	songs = []
	for mp3 in mp3s:
		songs.append(Song(mp3[0],mp3[1]))

	return songs

def getMp3ById(id):
	connection = _getConnection()

	try:
		cursor = _getCursor(connection)
		rowId = (id,)

		cursor.execute("SELECT name "
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

def _getCursor(connection):
	return connection.cursor()

def _getConnection():
	return sqlite3.connect(_dbName)

def _sanitizeString(value):
	return "'{0}'".format(value)