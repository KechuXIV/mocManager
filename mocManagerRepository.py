import sqlite3

_dbSqlFileName = 'mp3Library.sql'
_dbName = 'mp3Library.db'

def createDatabase():
	createDatabaseQuery = open(_dbSqlFileName, 'r').read()
	execute(createDatabaseQuery)

def selectAllMp3s():
	query = "SELECT mp3Id, title, artist, fileName, path " \
	"FROM mp3s"

	return execute(query)

def deleteAllMp3s():
	query = "DELETE FROM mp3s"

	return execute(query)

def insertMp3s(Mp3s):
	query = "INSERT INTO mp3s " \
	"(title, artist, fileName, path) " \
	"VALUES " \
	"(?, ?, ?, ?)"

	for mp3 in mp3s:
		execute(query, (mp3.title, mp3.artist, mp3.file, mp3.path))

def updateMp3s():
	pass

def deleteMp3s():
	pass

def insertPlaylists(playlists):
	query = "INSERT INTO playlists " \
	"(name, description) " \
	"VALUES " \
	"(?, ?)"

	for playlists in playlists
		execute(query, (playlist.name, playlist.description))

def updatePlaylists():
	pass

def deletePlaylists():
	pass

def instertMp3sInPlaylists(playlist):
	i = 0
	query = "INSERT INTO playlistsMp3s " \
	"(mp3Id, playlistId, position) " \
	"VALUES " \
	"(?, ?)"

	for mp3 in playlist.mp3s:
		execute(query, (mp3Id, playlist.playlistId, i++))

def execute(sqlQuery):
	connection = sqlite3.connect(_dbName)
	try:
		cursor = connection.cursor()
		cursor.execute(sqlQuery)

		return cursor.fetchall()
	except Exception, e:
		connection.rollback()
		raise e
	finally:
		connection.commit()

def executeWithValues(sqlQuery, values):
	print(sqlQuery)
	print(values)