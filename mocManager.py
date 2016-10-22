import os
import subprocess
import logging
import musicLibrary

_mocp = "mocp"
_playNow = "-l"
_startServer = "-F"
_stopServer = "-X"
_togglePause = "-G"
_enqueue = "-q"
_next = "-f"
_previous = "-r"
_goToSeconds = "-k"
_getInfo = "-i"

def starServer(mp3Id):
	subprocess.call([_mocp, _starServer])

def stopServer(mp3Id):
	subprocess.call([_mocp, _stopServer])

def playMp3(mp3Id):
	mp3 = musicLibrary.getMp3ById(mp3Id)
	fullPath = os.path.join(mp3.path, mp3.fileName)
	print(mp3Path)
	#subprocess.call([_mocp, _playNow, mp3Path])

def togglePause(mp3Id):
	subprocess.call([_mocp, _togglePause])

def enqueue(mp3Id):
	mp3Path = musicLibrary.getMp3ById(mp3Id)
	subprocess.call([_mocp, _enqueue, mp3Path])

def playNext(mp3Id):
	subprocess.call([_mocp, _next])

def playPrevious(mp3Id):
	subprocess.call([_mocp, _previous])

def goToSeconds(seconds):
	subprocess.call([_mocp, _goToSeconds, str(seconds)])

def getInfo(mp3Id):
	subprocess.call([_mocp, _getInfo])
