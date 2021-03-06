import logging
import falcon
import mocManager as mm
import musicLibrary as ml
import json
from mocAction import MocAction as ma

class MocManagerController(object):

	def __init__(self):
		self.logger = logging.getLogger('mocManagerApi.' + __name__)
		self.actions = {
			ma.PLAY_NOW: mm.playMp3,
			ma.TOGGLE_PAUSE_PLAY: mm.togglePause,
			ma.ENQUEUE: mm.enqueue,
			ma.NEXT: mm.playNext,
			ma.PREVIOUS: mm.playPrevious,
			ma.GO_TO_SECONDS: mm.goToSeconds,
			ma.INFO: mm.getInfo,
		}

	def on_get(self, req, resp, user_id):
		print("Entro Por Get")
		songs = ml.getMp3s()

		resp.body = json.dumps([song.__dict__ for song in songs])
		#resp.body = json.dumps(songs[0].__dict__)

		resp.set_header('Powered-By', 'Falcon')
		resp.status = falcon.HTTP_200

	def on_post(self, req, resp, user_id):
		try:
			print("Entro Por post")
			request = req.context['doc']
			print("Request es {0}".format(request))
			action = int(request['Action'])
			print("Action es {0}".format(action))

			#if not action in range(0,5):
			#	req.context['result'] = "Invalid ateration"
			#else:
			#	mp3Path = int(request['Mp3'])
		#		print("mp3Path es {0}".format(mp3Path))
		#		self.actions[action](mp3Path)

		except Exception as ex:
			#self.logger.error(ex)
			raise ex

		resp.set_header('Powered-By', 'Falcon')
		resp.status = falcon.HTTP_200
