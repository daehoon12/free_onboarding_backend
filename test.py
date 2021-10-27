import unittest
import requests
import json

class UnitTest(unittest.TestCase):
    def setUp(self):
        self.host = 'http://127.0.0.1:5000/'
        self.header = {"Content-Type": "application/json" }

        self.user_info = {
            'name':'Daehoon',
            'password':'1234'
        }

        self.post = {
            'id' : 'Daehoon',
            'data' : 'study!'
        }

        self.update_post={
                "id": "Daehoon",
                "post_no": 1,
                "data": "studydsdadsadasdas",
                "created_date": "21-10-26 13:38:45",
                "modified_date": "21-10-26 13:38:45"
        }

        self.delete_info = {
            "id": "Daehoon",
            "post_no": 1,
        }

        self.db = []
    def test_case1(self): # register
        response = requests.post(self.host + '/auth/register', headers = self.header, data=json.dumps(self.user_info))
        data = json.loads(response.text)
        # print(data)
        assert data['Authorization'] # 실패 시 키 에러

    def test_case2(self): # login
        response = requests.post(self.host + '/auth/login', headers=self.header, data=json.dumps(self.user_info))
        data = json.loads(response.text)
        # print(data)
        assert data['Authorization'] # 실패 시 키 에러

    def test_case3(self): # create
        response = requests.post(self.host + '/posts', headers=self.header, data=json.dumps(self.post))
        data = json.loads(response.text)
        assert data['id'] == self.post['id'] # 실패 시 키 에러

    def test_case4(self):  # update
        response = requests.put(self.host + '/posts/1', headers=self.header, data=json.dumps(self.update_post))
        data = json.loads(response.text)
        # print(data)
        assert data['id'] == self.update_post['id']  # 실패 시 키 에러

    def test_case5(self): # delete
        response = requests.delete(self.host + '/posts/1', headers=self.header, data=json.dumps(self.delete_info))
        data = json.loads(response.text)
        assert data['delete'] # 실패 시 키 에러

    def test_case6(self): # read
        params = {'limit':30, 'offset':0}
        response = requests.get(self.host + '/posts', headers=self.header, params=params)
        data = json.loads(response.text)
        # print(data)
        assert data['count'] # 실패 시 assertion

