import requests

class Auth:
    url = 'https://api.instagram.com/oauth/access_token'
    def __init__(self,code):
        self.code = code
        self.data = {
            'client_id': '839fc593c5954f30819699e1a4f1a2fe',
            'client_secret': '81835373dbf84be496178159f199cf81',
            'grant_type': 'authorization_code',
            'redirect_uri': 'http://127.0.0.1:5000/',
            'code': self.code
        }

    def req(self):
        result = requests.post(self.url, self.data)
        json = result.json()
        return json['access_token']
