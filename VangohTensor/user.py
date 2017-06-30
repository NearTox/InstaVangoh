import requests

class User:
    urltop = 'https://api.instagram.com/v1/users/self/media/recent/'
    url_user = 'https://api.instagram.com/v1/users/self/'
    count = 5

    def __init__(self, token):
        self.token = token
        self.data = {
            'access_token': self.token,
            'count': self.count
        }

    def getTop(self):
        result = requests.get(self.urltop, self.data)
        return result.json()

    def getUsername(self):
        data = {
            'access_token': self.token
        }
        result = requests.get(self.url_user, data)
        json = result.json()
        return json['data']['full_name']
