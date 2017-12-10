import unittest
import requests
import json

class TestApi(unittest.TestCase):

    def __init__(self, *a, **kw):
	    super(TestApi, self).__init__(*a, **kw)
	    self.host = 'demo6144383.mockable.io'
	    self.members = 'members'
	    self.member = 'member'
	    self.id = '1'
	    self.urlmembers = 'https://{}/{}'.format(self.host, self.members)
	    self.urlmember = 'https://{}/{}/{}'.format(self.host, self.member, self.id)

    def test_1_member(self):
    	status_code, member = self._get_member()
    	self.assertEqual(status_code, 200)
    	self.assertEqual(member.get('id'), 1)
      
    def test_members(self):
    	status_code, members = self._get_members()
    	self.assertEqual(status_code, 200)
    	self.assertGreater(len(members.get('team_members')), 1)

    def _get_members(self):
    	_url = self.urlmembers
    	_response = requests.get(_url)
    	return _response.status_code, _response.json() 

    def _get_member(self):
    	_url = self.urlmember
    	_response = requests.get(_url)
    	return _response.status_code, _response.json()



if __name__ == '__main__':
   unittest.main(verbosity=2)