__author__ = 'Frederick'

import json
import requests


class Postman(object):

    """This method returns r and  json encoded response"""
    def request_(url):
        r = requests.get(url)
        r.raise_for_status()
        assert(r.status_code, 200)
        return json.loads(r.text)
