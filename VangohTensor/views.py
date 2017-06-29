from flask import Flask,request,redirect,url_for,render_template
import requests
from VangohTensor import app

class Auth:
	url = 'https://api.instagram.com/oauth/access_token'
	def __init__(self,code):
		self.code = code
		self.data = {'client_id':'839fc593c5954f30819699e1a4f1a2fe',
		'client_secret':'81835373dbf84be496178159f199cf81',
		'grant_type':'authorization_code',
		'redirect_uri':'http://127.0.0.1:5000/',
		'code':self.code}
	def req(self):
		r = requests.post(self.url,self.data)
		json = r.json()
		return json['access_token']

class User:
	urltop = 'https://api.instagram.com/v1/users/self/media/recent/'
	count = 5

	def __init__(self,token):
		self.data = {'access_token':token,
					'count':self.count}

	def getTop(self):
		r = requests.get(self.urltop,self.data)
		return r.json()

@app.route('/login')
def login():
	return render_template('login.html')

@app.route('/')
def getToken():
    code = request.args.get('code')
    token = Auth(code)
    r = redirect("/home")
    r.set_cookie('Token',token.req())
    return r
    
@app.route('/home')
def getImages():
	cookie = request.cookies.get('Token')
	user = User(cookie)
	resp = user.getTop()
	datas = resp['data']
	for post in datas:
		data = post['images']['standard_resolution']['url']
	
	return render_template('index.html', datas=datas)

