import os
import subprocess
import logging
import musicLibrary

mocp = "mocp"
playNow = "-l"
startServer = "-F"
stopServer = "-X"
togglePause = "-G"
enqueue = "-q"
next = "-f"
previous = "-r"
goToSeconds = "-k"
getInfo = "-i"

def starServer(mp3Id):
	subprocess.call([mocp, starServer])

def stopServer(mp3Id):
	subprocess.call([mocp, stopServer])

def playMp3(mp3Id):
	mp3Path = musicLibrary.getMp3ById(mp3Id)
	subprocess.call([mocp, playNow, mp3Path])

def togglePause(mp3Id):
	subprocess.call([mocp, togglePause])

def enqueue(mp3Id):
	mp3Path = musicLibrary.getMp3ById(mp3Id)
	subprocess.call([mocp, enqueue, mp3Path])

def playNext(mp3Id):
	subprocess.call([mocp, next])

def playPrevious(mp3Id):
	subprocess.call([mocp, previous])

def goToSeconds(seconds):
	subprocess.call([mocp, goToSeconds, seconds])

def getInfo(mp3Id):
	subprocess.call([mocp, getInfo])
