import json
import logging
import uuid
from wsgiref import simple_server
from mocManagerController import MocManagerController

import falcon
import requests


class StorageError(object):
	@staticmethod
	def handle(ex, req, resp, params):
		description = ('Sorry, couldn\'t write your thing to the '
			'database. It worked on my box.')

		raise falcon.HTTPError(falcon.HTTP_725,
			'Database Error',
			description)

class SinkAdapter(object):

	engines = {
		'ddg': 'https://duckduckgo.com',
		'y': 'https://search.yahoo.com/search',
	}

	def __call__(self, req, resp, engine):
		url = self.engines[engine]
		params = {'q': req.get_param('q', True)}
		result = requests.get(url, params=params)

		resp.status = str(result.status_code) + ' ' + result.reason
		resp.content_type = result.headers['content-type']
		resp.body = result.text

class AuthMiddleware(object):

	def process_request(self, req, resp):
		print("Bellesa nene")
		token = req.get_header('Authorization')
		account_id = req.get_header('Account-ID')

		challenges = ['Token type="Fernet"']

		if token is None:
			print("2")
			description = ('Please provide an auth token '
						   'as part of the request.')

			raise falcon.HTTPUnauthorized('Auth token required',
										  description,
										  challenges,
										  href='http://docs.example.com/auth')

		if not self._token_is_valid(token, account_id):
			print("3")
			description = ('The provided auth token is not valid. '
						   'Please request a new token and try again.')

			raise falcon.HTTPUnauthorized('Authentication required',
										  description,
										  challenges,
										  href='http://docs.example.com/auth')

	def _token_is_valid(self, token, account_id):
		return True  # Suuuuuure it's valid...

class RequireJSON(object):

	def process_request(self, req, resp):
		if not req.client_accepts_json:
			raise falcon.HTTPNotAcceptable(
				'This API only supports responses encoded as JSON.',
				href='http://docs.examples.com/api/json')

		if req.method in ('POST', 'PUT'):
			if 'application/json' not in req.content_type:
				raise falcon.HTTPUnsupportedMediaType(
					'This API only supports requests encoded as JSON.',
					href='http://docs.examples.com/api/json')


class JSONTranslator(object):

	def process_request(self, req, resp):
		# req.stream corresponds to the WSGI wsgi.input environ variable,
		# and allows you to read bytes from the request body.
		#
		# See also: PEP 3333
		if req.content_length in (None, 0):
			# Nothing to do
			return

		body = req.stream.read()
		if not body:
			raise falcon.HTTPBadRequest('Empty request body',
										'A valid JSON document is required.')

		try:
			req.context['doc'] = json.loads(body.decode('utf-8'))

		except (ValueError, UnicodeDecodeError):
			raise falcon.HTTPError(falcon.HTTP_753,
								'Malformed JSON',
								'Could not decode the request body. The '
								'JSON was incorrect or not encoded as '
								'UTF-8.')

	def process_response(self, req, resp, resource):
		if 'result' not in req.context:
			return

		resp.body = json.dumps(req.context['result'])

def max_body(limit):

	def hook(req, resp, resource, params):
		length = req.content_length
		if length is not None and length > limit:
			msg = ('The size of the request is too large. The body must not '
				'exceed ' + str(limit) + ' bytes in length.')

			raise falcon.HTTPRequestEntityTooLarge(
				'Request body is too large', msg)

	return hook


# Configure your WSGI server to load "things.app" (app is a WSGI callable)
app = falcon.API(middleware=[
	AuthMiddleware(),
	RequireJSON(),
	JSONTranslator(),
])

mocManagerController = MocManagerController()
app.add_route('/{user_id}/MocManager', mocManagerController)

# If a responder ever raised an instance of StorageError, pass control to
# the given handler.
app.add_error_handler(StorageError, StorageError.handle)

# Proxy some things to another service; this example shows how you might
# send parts of an API off to a legacy system that hasn't been upgraded
# yet, or perhaps is a single cluster that all data centers have to share.
sink = SinkAdapter()
app.add_sink(sink, r'/search/(?P<engine>ddg|y)\Z')

# Useful for debugging problems in your API; works with pdb.set_trace(). You
# can also use Gunicorn to host your app. Gunicorn can be configured to
# auto-restart workers when it detects a code change, and it also works
# with pdb.
if __name__ == '__main__':
	httpd = simple_server.make_server('127.0.0.1', 8000, app)
	httpd.serve_forever()