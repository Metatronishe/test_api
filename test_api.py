import unittest
import requests
import json
from page_object import PageObject

class TestApi(unittest.TestCase):

	success = 200
		

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
    	self.assertEqual(status_code, success)
    	self.assertEqual(member.get(listid), 1)
      
    def test_members(self):
    	status_code, members = self._get_members()
    	self.assertEqual(status_code, success)
    	self.assertGreater(len(members.get(listall)), 1)

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