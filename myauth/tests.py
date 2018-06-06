from django.test import TestCase
import json

from django.contrib.auth.models import User

class AuthTests(TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_registerUserPass(self):
        data = {
                "username": "abir",
                "password": "adfa",
                "email": "abir@a.com",
                "first_name": "Abir",
                "last_name": "Ahmed"
            }
        response = self.client.post('/api/v1/myauth/register/', json.dumps(data), content_type="application/json")
        decoded = json.loads(response.content.decode())

        self.assertEqual(decoded["username"], data["username"])

    def test_registerUserNoPassword(self):
        data = {
                "username": "abir",
                "password": "",
                "email": "abir@a.com",
                "first_name": "Abir",
                "last_name": "Ahmed"
            }
        response = self.client.post('/api/v1/myauth/register/', json.dumps(data), content_type="application/json")
        decoded = json.loads(response.content.decode())

        self.assertEqual(decoded['password'], ['This field may not be blank.'])

# Create your tests here.


