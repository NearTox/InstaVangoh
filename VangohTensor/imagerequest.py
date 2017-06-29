import requests

url = 'https://api.instagram.com/oauth/access_token'
data = {'client_id':'839fc593c5954f30819699e1a4f1a2fe',
		'client_secret':'81835373dbf84be496178159f199cf81',
		'grant_type':'authorization_code',
		'redirect_uri':'http://127.0.0.1:5000/',
		'code':'418094c705ba49b9843cc213f72fe668'}
r = requests.post(url,data)
json = r.json()
token = json['access_token']