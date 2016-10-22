from sqlalchemy import *

def createDb():
	db = create_engine('sqlite:///tutorial.db')

	db.echo = False  # Try changing this to True and see what happens

	metadata = MetaData(db)

	playlistsMp3s = Table('playlistsMp3s', metadata,
		Column('playlistId', Integer, primary_key=True),
		Column('mp3Id', Integer, nullable=False),
		Column('position', Integer),
	)
	playlistsMp3s.create()

	playlists = Table('playlists', metadata,
		Column('playlistId', Integer, primary_key=True),
		Column('name', String(40), nullable=False),
		Column('description', String(120)),
	)
	playlists.create()

	mp3s = Table('mp3s', metadata,
		Column('mp3Id', Integer, primary_key=True),
		Column('title', String(40), nullable=False),
		Column('artist', String(40), nullable=False),
		Column('fileName', String(40), nullable=False),
		Column('path', String(250), nullable=False),
	)
	mp3s.create()