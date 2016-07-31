import os
import sqlite3

_dbName = 'mp3Library.db'
_musicPath = "/{0}".format(os.path.join("","home","kechunet","Music"))

def createDatabase():
	connection = _getConnection()
	cursor = _getCursor(connection)

	cursor.execute("CREATE TABLE mp3s "
		"(name text, path text)")

	_closeAndCommit(connection)

def getMp3InMusic():
	os.listdir(musicPath)
	mp3Files = [file for file in os.listdir(musicPath) if file.endswith(".mp3")]
	return mp3Files

def saveMp3s():
	connection = _getConnection()
	cursor = _getCursor(connection)

	mp3Files = getMp3InMusic()

	for mp3File in mp3Files:
		value = (_sanitizeString(mp3File), _sanitizeString(musicPath))
		cursor.execute("INSERT INTO mp3s "
			"VALUES "
			"(?, ?)",value)

	_closeAndCommit(connection)

def getMp3s():
	connection = _getConnection()
	cursor = _getCursor(connection)

	cursor.execute("SELECT rowId, name "
			"FROM "
			"mp3s ")

	mp3s = cursor.fetchall()

	_closeAndCommit(connection)

	return mp3s

def getMp3ById(id):
	connection = _getConnection()
	cursor = _getCursor(connection)
	rowId = (id,)

	cursor.execute("SELECT name "
			"FROM "
			"mp3s "
			"WHERE "
			"rowId = ? ", rowId)

	mp3Name = cursor.fetchone()[0]

	_closeAndCommit(connection)

	return os.path.join(_musicPath, mp3Name)

def _getCursor(connection):
	return connection.cursor()

def _getConnection():
	return sqlite3.connect(_dbName)

def _closeAndCommit(connection):
	connection.commit()
	connection.close()

def _sanitizeString(value):
	return "'{0}'".format(value)