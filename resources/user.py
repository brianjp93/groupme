"""user.py
"""
import requests


class User:

    def __init__(self, parent):
        self.parent = parent
        self.base = '{}/users'.format(self.parent.base)

    def me(self):
        """Get information about the user.

        Returns
        -------
        Response

        """
        url = '{}/me'.format(self.base)
        params = {
            'token': self.parent.token,
        }
        r = requests.get(url, headers=self.parent.headers, params=params)
        return r