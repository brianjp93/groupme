"""groupme.py
"""
import resources

__author__ = 'Brian Perrett'
__date__ = '19-04-2018'


class Client:

	base = 'https://api.groupme.com/v3'
	headers = {'Content-Type': 'application/json'}

	def __init__(self, token):
		self.token = token

		# resources
		self.group = resources.Group(self)
