"""groupme.py
"""
import resources

__author__ = 'Brian Perrett'
__date__ = '19-04-2018'


class Client:

	base = 'https://api.groupme.com/v3'
	headers = {'Content-Type': 'application/json'}

	def __init__(self, token, client_id=None):
		self.token = token
		self.client_id = client_id

		# resources
		self.group = resources.Group(self)

	def get_auth_url(self):
		"""Get URL for granting access to a user's data.

		Returns
		-------
		str

		"""
		url = 'https://oauth.groupme.com/oauth/authorize?client_id={}'.format(self.client_id)
		return url

	