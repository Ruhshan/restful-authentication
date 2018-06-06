from django.test import TestCase
import json

from django.contrib.auth.models import User

class AuthTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user('john', 'lennon@thebeatles.com', 'johnpassword')
        self.user.save()

        data = {
            "username":"john",
            "password":"johnpassword"
        }
        response = self.client.post('/api/v1/myauth/login/', json.dumps(data), content_type="application/json")
        self.token = json.loads(response.content.decode())['token']

    def tearDown(self):
        self.user.delete()

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

    def test_userloginValid(self):
        data = {
            "username":"john",
            "password":"johnpassword"
        }
        response = self.client.post('/api/v1/myauth/login/', json.dumps(data), content_type="application/json")
        decoded = json.loads(response.content.decode())
        self.assertIn('token', decoded.keys())

    def test_userloginInValid(self):
        data = {
            "username":"john",
            "password":"johnpasswordnone"
        }
        response = self.client.post('/api/v1/myauth/login/', json.dumps(data), content_type="application/json")
        decoded = json.loads(response.content.decode())
        self.assertNotIn('token', decoded.keys())

    def test_logout(self):
        data={
            'user': self.user.username
        }
        response = self.client.post('/api/v1/myauth/logout/', json.dumps(data), content_type="application/json", HTTP_AUTHORIZATION='JWT {}'.format(self.token))
        decoded = response.content.decode()
        
        self.assertEqual(decoded, '"User is logged out"')


# Create your tests here.


