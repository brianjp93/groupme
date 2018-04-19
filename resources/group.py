"""group.py
"""
import requests


class Group:

	def __init__(self, parent):
		self.parent = parent
		self.base = '{}/groups'.format(self.parent.base)

	def get(self, page=1, per_page=10, omit=[]):
		"""Get a list of groups and information about each.

		Parameters
		----------
		page : int
		per_page : int
		omit : list
			Only valid entry is "memberships" right now

		Returns
		-------
		Response

		"""
		url = '{}'.format(self.base)
		params = {
			'page': page,
			'per_page': per_page,
			'token': self.parent.token,
		}
		if omit:
			params['omit'] = ','.join(omit)
		r = requests.get(url, headers=self.parent.headers, params=params)
		return r

	def get_messages(self, group_id, before_id=None, since_id=None, after_id=None, limit=20):
		"""Get messages from a group chat.

		Parameters
		----------
		group_id : int
		before_id : str
		since_id : str
		after_id : str
		limit : int
			max : 100
			default : 20

		Returns
		-------
		Response

		"""
		url = '{}/{}/messages'.format(self.base, group_id)
		params = {'limit': limit, 'token': self.parent.token}
		if before_id is not None:
			params['before_id'] = before_id
		if since_id is not None:
			params['since_id'] = since_id
		if after_id is not None:
			params['after_id'] = after_id
		r = requests.get(url, headers=self.parent.headers, params=params)
		return r
