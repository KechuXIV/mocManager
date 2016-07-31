import logging
import falcon
import mocManager as mm
import musicLibrary as ml
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
		result = ml.getMp3s()
		req.context['result'] = result

		resp.set_header('Powered-By', 'Falcon')
		resp.status = falcon.HTTP_200

	#@falcon.before(max_body(64 * 1024))
	def on_post(self, req, resp, user_id):
		try:
			request = req.context['doc']
			action = int(request['Action'])
			mp3Path = int(request['Mp3'])
			self.actions[action](mp3Path)
		except Exception as ex:
			print(ex)
			self.logger.error(ex)

		resp.set_header('Powered-By', 'Falcon')
		resp.status = falcon.HTTP_200
